from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Home page application Learning lof"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Displays list all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Displays one theame and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Verifying that a topic belong to the current user.
    check_topic_owner(request, topic.owner)

    entries = topic.entry_set.order_by("-date_added")
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Defines new topic."""
    if request.method != 'POST':
        # No date was sent; an empty form is created.
        form = TopicForm()
    else:
        # Post data sent; data processed.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Output empty or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add new entry to the concrete topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    if request.method != 'POST':
        # Data don't sent; blank form is created.
        form = EntryForm()
    else:
        # Sent data POST; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Output empty or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic.owner)

    if request.method != 'POST':
        # Source query; the form is filled in with current record data.
        form = EntryForm(instance=entry)
    else:
        # Set data POST
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(request, owner):
    if owner != request.user:
        raise Http404
