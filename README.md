# Whatschat
A simple chat with Vue and Django 

To run this, you have to install rabbitmq-server. All you need to do is follow Osaetin Daniel's tutorial.
<a>https://danidee10.github.io/2018/01/01/realtime-django-1.html</a>

I'm just add Vuetify for the front-end and modify this a litte bit in the back-end.
To run this project, you have to run the following command in your Terminal:<br><br>
<code>root@: rabbitmq-server --detached</code><br>
<code>root@: python3 manage.py runserver</code><br><br>
cd to ./chat folder, and run<br>
<code>root@: uwsgi --http :8081 --module websocket --master --processes 4 --uid <YOUR_USERNAME></code><br>
<code>root@: celery -A chat worker -l info</code><br><br>

Open your browser, enter link:<br>
<code>http://localhost:8080</code>

Preview
<img src='/preview/login_form.png'></img><br>
<img src='/preview/welcome.png'></img><br>
<img src='/preview/chatwithother.png'></img><br>
<img src='/preview/chat.png'></img><br>

Happy codings!
