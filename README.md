<h1 class="gap">0x00. AirBnB clone - The console</h1>
<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220706T051044Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4ee8af10b50bf7ced4624a79beb01e8fd7811e2b0a7b2ad159d031869f4ff017" width="517" height="218" /></p>
<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>
<p>This is the first step towards building your first full web application: the&nbsp;<strong>AirBnB clone</strong>. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip;</p>
<p>Each task is linked and will help you to:</p>
<ul>
<li>put in place a parent class (called&nbsp;<code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>,&nbsp;<code>State</code>,&nbsp;<code>City</code>,&nbsp;<code>Place</code>&hellip;) that inherit from&nbsp;<code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage.</li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>
<h3>What&rsquo;s a command interpreter?</h3>
<p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>
<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc&hellip;</li>
<li>Do operations on objects (count, compute stats, etc&hellip;)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>
<h2>More Info</h2>
<h3>Execution</h3>
<p>Your shell should work like this in interactive mode:</p>
<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>
<p>But also in non-interactive mode: (like the Shell project in C)</p>
<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>
<p>All tests should also pass in non-interactive mode:&nbsp;<code>$ echo "python3 -m unittest discover tests" | bash</code></p>
<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220706%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220706T051044Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c73b5af10026ce8a3af2a47a646835a86a713f15f7698bd6267f8f5d255e1ea3" alt="" /></p>
<h1 style="color: #5e9ca0;">&nbsp;</h1>
<p>&nbsp;</p>
