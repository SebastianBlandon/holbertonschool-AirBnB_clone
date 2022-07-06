<h1 class="gap">0x00. AirBnB clone - The console</h1>
<p><img src="https://bn1305files.storage.live.com/y4mBZR2qGhr3lq4SPgnxJopyyHtZzlMvrbMZ5dilioNByiUNFB7nnxvWGDBpKTFGexwr5bv-frUJk5BVifP0imGy_YT6h-hiORX5Le75x5-AE5iAO_N558BjQhWICc9RrAuDVFjfR9C8dxTpWjOTkHMSj6ZpRO3kgka67OFsXaYLNkTbuO4jqAA1isrlsJkOuQ4_BGCv10UBCtjyGAgPc85SOOdwP2yUERQ7JE9Ha2IoHc?encodeFailures=1&width=1920&height=810" width="517" height="218" /></p>
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
<p><img src="https://bn1305files.storage.live.com/y4mN6nr7GPEaSdKtLb2zk_Rmx3KzgggzaO_o8gCxCxuRbZGZ84zHfdsDM47t9-DiJCNWPc-EZl7NDOpbMKlsNitsthxTvTVoFSmp11upbDDWVLYhhhO7y5a9ruCBZhBGUKLXGHYgzE2d1dmiblA6kVPe_nLjUsPtmeBYSIeu0SrO4lXJKYISozaeTA1nk8FLHQ8IVFau8Ymk1w42wi2MUJEQZYA9Ogdrq53asavvExjkGk?encodeFailures=1&width=1257&height=669" alt="" /></p>
<h1 style="color: #5e9ca0;">&nbsp;</h1>
<p>&nbsp;</p>
