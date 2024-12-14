from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
articles = [
    {
        "id": 1,
        "title": "Introduction to Artificial Intelligence",
        "content": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions.",
        "timestamp": "2022-01-01T12:00:00",
    },
    {
        "id": 2,
        "title": "The Future of Space Exploration",
        "content": "Space exploration has been a fascinating topic for centuries, and with advancements in technology, we are now closer than ever to exploring the cosmos.",
        "timestamp": "2022-02-15T10:00:00",
    },
    {
        "id": 3,
        "title": "The Impact of Social Media on Society",
        "content": "Social media has revolutionized the way we communicate and interact with each other, but it also has its downsides.",
        "timestamp": "2022-03-20T14:00:00",
    },
    {
        "id": 4,
        "title": "The Benefits of Meditation and Mindfulness",
        "content": "Meditation and mindfulness have been shown to have numerous benefits for both physical and mental health.",
        "timestamp": "2022-04-10T16:00:00",
    },
    {
        "id": 5,
        "title": "The Science Behind Climate Change",
        "content": "Climate change is one of the most pressing issues of our time, and understanding the science behind it is crucial for finding solutions.",
        "timestamp": "2022-05-05T12:00:00",
    },
    {
        "id": 6,
        "title": "The History of the Internet",
        "content": "The internet has come a long way since its inception in the 1960s, and its impact on modern society cannot be overstated.",
        "timestamp": "2022-06-01T10:00:00",
    },
    {
        "id": 7,
        "title": "The Benefits of Reading for Personal Growth",
        "content": "Reading is one of the most effective ways to expand your knowledge, improve your critical thinking skills, and enhance your personal growth.",
        "timestamp": "2022-07-15T14:00:00",
    },
    {
        "id": 8,
        "title": "The Importance of Mental Health Awareness",
        "content": "Mental health awareness is crucial for reducing stigma, promoting understanding, and encouraging people to seek help when they need it.",
        "timestamp": "2022-08-10T16:00:00",
    },
    {
        "id": 9,
        "title": "The Future of Renewable Energy",
        "content": "Renewable energy is becoming increasingly important as the world transitions away from fossil fuels and towards more sustainable sources of energy.",
        "timestamp": "2022-09-05T12:00:00",
    },
    {
        "id": 10,
        "title": "The Impact of Technology on Education",
        "content": "Technology has transformed the way we learn, making education more accessible, engaging, and effective.",
        "timestamp": "2022-10-01T10:00:00",
    },
]


def home(request):
    return render(request, "posts/home.html")


def hello_world(request):
    return HttpResponse("Hello Aliens!")


def article_list(request):
    return render(request, "posts/articles.html", {"articles": articles})


def post(request, id):
    print(f"Type : {type(id)}")
    id_is_valid = False
    final_art = []
    for art in articles:
        print(f"ART : {art} {art['id']}")
        if art["id"] == id:
            id_is_valid = True
            final_art.clear()
            final_art.append(art)

    if id_is_valid:
        print(f"Article With id : {id} --> \n {articles[7]}")
        return render(request, "posts/articles.html", {"articles": final_art})
    else:
        return HttpResponseNotFound("Post Not Available!")


def reverse_redirect(request, id):
    print(f"reverse redirect {id}")
    url = reverse("postById", args=[id])
    return HttpResponseRedirect(url)
