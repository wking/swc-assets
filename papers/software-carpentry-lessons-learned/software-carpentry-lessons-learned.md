# Software Carpentry: Lessons Learned

* Azalee Bostroem (Space Telescope Science Institute / bostroem@stsci.edu)
* Chris Cannam (Queen Mary, University of London / chris.cannam@eecs.qmul.ac.uk)
* Stephen Crouch (Software Sustainability Institute / s.crouch@software.ac.uk)
* Matt Davis (Space Telescope Science Institute / mrdavis@stsci.edu)
* Luis Figueira (Queen Mary, University of London / luis.figueira@eecs.qmul.ac.uk)
* Richard "Tommy" Guy (Wave Accounting / richardtguy84@gmail.com)
* Edward Hart (University of British Columbia / ehart@zoology.ubc.ca)
* Neil Chue Hong (Software Sustainability Institute / N.ChueHong@epcc.ed.ac.uk)
* Katy Huff (University of  Wisconsin / khuff@cae.wisc.edu)
* Michael Jackson (Edinburgh Parallel Computing Centre / michaelj@epcc.ed.ac.uk)
* Justin Kitzes (University of California, Berkeley / jkitzes@berkeley.edu)
* Stephen McGough (University of Newcastle / stephen.mcgough@newcastle.ac.uk) 
* Lex Nederbragt (University of Oslo / lex.nederbragt@ibv.uio.no)
* Tracy Teal (Michigan State University / tracyt@idyll.org)
* Ben Waugh (University College London / b.waugh@ucl.ac.uk)
* Lynne J. Williams (Rotman Research Institute / lwilliams@research.baycrest.org)
* Ethan White (Utah State University / ethan@weecology.org)
* Greg Wilson (Software Carpentry / gvwilson@software-carpentry.org)

## Abstract

FIXME: write abstract

## Introduction

Between January 2012 and July 2013,
Software Carpentry ran 92 two-day workshops on basic computing skills.
More than 100 people helped over 3000 scientists learn about
program design,
task automation,
version control,
testing,
and the unglamorous but essential foundations
for high-performance computing,
data science,
and anything with "cloud" in its name.
This article summarizes how we teach,
what we've learned from doing it,
and what we plan to do next.

## Context: The Missing Side of the Triangle

Back in 2010, Moshe Vardi wrote an opinion piece titled "<a href="http://cacm.acm.org/magazines/2010/9/98038-science-has-only-two-legs/fulltext">Science Has Only Two Legs</a>",
in which he argued that computational science is just another form of experimental science,
and that programs should be held to the same standards as other pieces of experimental apparatus.
We're firmly in this camp.

In March 2012,
<a href="http://www.hanselman.com/blog/AboutMe.aspx">Scott Hanselman</a> wrote a blog post titled
<a href="http://www.hanselman.com/blog/DarkMatterDevelopersTheUnseen99.aspx">Dark Matter Developers: The Unseen 99%</a>
In it, he said:

>    [We] hypothesize that there is another kind of developer than the ones we meet all the time.
>    We call them Dark Matter Developers.
>    They don't read a lot of blogs,
>    they never write blogs,
>    they don't go to user groups,
>    they don't tweet or facebook,
>    and you don't often see them at large conferences...
>    [A]s one of the loud-online-pushing-things-forward 1%,
>    I might think I need to find these Dark Matter Developers and explain to them how they need to get online!
>    Join the community!
>    Get a blog, start changing stuff, mix it up!
>    But...those dark matter 99% have a lot to teach us about GETTING STUFF DONE...
>    They aren't chasing the latest beta or pushing any limits,
>    they are just producing.

I'm not as optimistic as Scott, at least, not when it comes to scientific computing.
I agree that 95% spend their time with their heads down,
working hard,
instead of talking about using GPU clouds to personalize collaborative management of reproducible peta-scale workflows,
or some other permutation of currently-fashionable buzzwords.
It isn't even because they don't know there's a better way.
It's because for them, that better way is out of their reach.

A few weeks ago, John Cook <a href="http://www.johndcook.com/blog/2012/01/01/moores-law-squared/">posted</a> the following:

>    In a review of linear programming solvers from 1987 to 2002, Bob Bixby says that solvers benefited as much from algorithm improvements as from Moore's law:
>    Three orders of magnitude in machine speed and three orders of magnitude in algorithmic speed add up to six orders of magnitude in solving power.
>    A model that might have taken a year to solve 10 years ago can now solve in less than 30 seconds.

A million-fold speedup is pretty impressive, but faster hardware and better algorithms are only two sides to the triangle.
The third is development time, and while I think it has improved since 1987, I also think the speedup is measured in single-digit multiples, not orders of magnitude.

Which brings us, again, to <a href="http://en.wikipedia.org/wiki/Amdahl%27s_law">Amdahl's Law</a> and the purpose of Software Carpentry.
The time needed to produce a new computational result is <em>D+R</em>, where <em>D</em> is how long it takes to get the code to work and <em>R</em> is how long it takes that code to run.
(In practice, <em>R</em> doesn't go to zero for many interesting scientific applications, because scientists scale up their problems to keep running times constant.  As a colleague of mine once said, every simulation takes roughly one publication cycle to run.)
<em>R</em> depends on hardware and algorithms; as it goes to zero, the time required to get a new result is dominated by the time required to write, test, maintain, install, and configure software.
Reducing that is the "effiency" part of our long-term aim to improve novelty, efficiency, and trust.

Distinguish openness, reproducibility, and computational competence.

"It only takes a few minutes to show someone how to write a simple CGI script, or to tweak some PHP to modify a WordPress plugin."
Well, yes, but that's like saying that it only takes a few minutes to show someone how to start a car and get it out on the road.
It's what we have to teach people so that they can survive what happens next that takes time. 

----

Suppose you have a processing pipeline with three stages.
Each stage takes one second to run; what's its overall performance?
As Roger Hockney pointed out in the 1980s, that question isn't well formed.
What we really need to ask is,
how does its performance change as a function of the size of its input?
It takes 3 seconds to process one piece of data, 4 to process two, 5 to process three, and so on.
Inverting those numbers, its rate is 1/3 result per second for one piece of data, 2/4 = 1/2 result/sec for two, 3/5 for 3, etc.
If we draw this curve, we get:

Any pipeline's curve can be characterized by two values:
<em>r<sub>&infin;</sub></em>,
which is its performance on an infinitely large data set,
and <em>n<sub>1/2</sub></em>,
which is how much data we have to provide to get half of that theoretical peak performance.
Deep pipelines tend to have high <em>r<sub>&infin;</sub></em> (which is good),
but also high <em>n<sub>1/2</sub></em> (which is bad);
shallow pipelines are the reverse.

The more interesting measure is actually <em>p<sub>1/2</sub></em>,
which is how many programming hours it takes to reach half of a machine's theoretical peak performance.
On most machines,
and for most programmers,
the answer was and is "infinity",
since most programmers think they're doing well if they can ever achieve 20-25% of the performance that the manufacturer quotes for a piece of hardware.

This idea it underpins a lot of Software Carpentry.
Our goal is to increase researchers' <em>r<sub>&infin;</sub></em>,
i.e.,
to help them produce new science faster.
Our challenge is to minimize <em>p<sub>1/2</sub></em>,
so that researchers see benefits early.
In fact, our real challenge is that learners' performance over time actually looks like this:

That dip is due to Glass's Law:
every innovation initially slows you down.
If the dip is too deep,
or if it takes too long to recover from it,
most people go back to doing things the way they're used to,
because that's the safest bet.
But if learners are working in a group with their peers, they seem to be willing to trust us more (or for longer) than otherwise.
I don't think this is a case of not wanting to be the first to stop clapping;
I think instead that with a group of half a dozen or more,
the odds are good that <em>someone</em> is getting something out of the material at any particular moment, which gives everyone else a reason to carry on.

## Red, Red, Green Blue (or, How We Got Here)

In 1995--96,
Greg Wilson organized a series of articles titled,
"What Should Computer Scientists Teach to Physical Scientists and Engineers?"
[wilson1996][wilson1996].
The articles grew out of the frustration he felt working with scientists
who wanted to parallelize complex programs
but didn't know how to modularize their code,
test it,
or track changes
[wilson2006a][wilson2006a]---in short,
scientists who were trying to run before they could walk.

In response,
John Reynders
(then director of the Advanced Computing Laboratory at Los Alamos National Laboratory)
invited Wilson and Brent Gorda (now at Intel)
to teach a week-long course to LANL staff.
The course ran for the first time in July 1998,
and was repeated eight times over the next four years.
It eventually wound down because the principal players had all moved on to other responsibilities.

What we learned:

* An intensive week-long format works better for scheduling than for learning.
* We tried to teach traditional software engineering; it's the wrong thing for most scientists.

The Software Carpentry course materials
were updated and released under a Creative Commons license in 2004--05
thanks to a grant from the Python Software Foundation
[wilson2006b][wilson2006b].

Ran as a conventional term-long university course twice at the University of Toronto.

* Traffic: 1000-2000 unique visitors/month (with spikes correlated to courses).
* Online lecture notes aren't really useful: people want _lectures_.
* No Wikipedia effect: good lessons are narratives, not merely facts presented in sequence.
* An awkward fit at universities:
  * CS departments believe it's too easy (even though many of their grad students are no better at software dev than anyone else)
  * Other departments believe CS should offer it (it's clearly not chemistry)
  * And those departments won't make room: what do they take out?
  * For example, see blog/2012/12/computer-science-curricula-2013.html for a comparison with the ACM curriculum guidelines

Wilson rebooted Software Carpentry in May 2010
with support from
(Indiana University,
Michigan State University,
Microsoft,
MITACS,
Queen Mary University of London,
Scimatic,
SciNet,
SHARCNet,
and the UK Met Office.
More than 120 short video lessons were recorded during the following 12 months,
and six more week-long classes were run.
We also offered an online class three times
(before the term "MOOC" became widely known).

* Clear by mid-2011 that there was more demand for this kind of training than ever.
  * Data science, scientific blogging, open access publishing, alt metrics...
* Only a handful of other people (Orion Buske, Tommy Guy, Jason Montojo, Jon Pipitone, and Ethan White) contributed material.
* MOOC format was disappointing: only 5-10% of starters finished, most because fitting in "makework" around real work was hard.
* But once again, five eight-hour days are more wearying than enlightening.

Wilson spent much of the eight months from May to December 2011 rethinking
and reading the educational literature.
(Should have done this long before...)

With new support from the Sloan Foundation and Mozilla,
Software Carpentry rebooted again in January 2012.
This time,
the model was two-day "boot camps"
modeled on those pioneered by [The Hacker Within][thw],
a grassroots group of grad students helping grad students
at the University of Wisconsin -- Madison.
Shortening the boot camps made it possible for more people to attend,
and forced us to think much harder about what skills scientists really needed.

* Explain what we dropped: XML, web programming, OOP

Reaching more people also allowed us to recruit more instructors
from boot camp participants.
The results are dramatically better than previous iterations.
Software Carpentry now has over 70 qualified instructors,
runs six or seven boot camps a month,
and is almost self-sustaining financially.

* Explain the "almost": host sites pay expenses, so that scales, but we need a central coordinator.
* Mention SSI.

## What We Do

So what does a typical boot camp look like?

* Two days, two instructors, helpers, forty people
  * As mentioned earlier,
    our instructors are all volunteers,
    so the only costs to host sites are travel and accommodation
    (and coffee, if they choose).
* Most boot camps are still free, but we are starting to use a $20 cover charge to discourage no-shows
  * Either we keep it, or we refund it to people who are there both days
  * Have to be careful not to trip over institutional wires (we charge so they do)
* Content varies, but a representative agenda is:
  * Day 1 a.m.:
    Introduction to Unix shell.
    We show participants a dozen basic commands,
    but the real aim is to introduce them to pipes,
    loops and history (to automate repetitive tasks),
    and the idea of scripting.
  * Day 1 p.m.:
    Version control for file sharing, collaboration, and reproducibility.
    Now mostly using Git and GitHub (see below).
  * Day 1 p.m.:
    If time permits,
    a quick intro to regular expressions using a graphical tool
    or to databases and SQL.
  * Day 2 a.m.:
    Introduction to Python,
    but the real goal is to show them when and why to develop code as a set of comprehensible, reusable functions.
  * Day 2 p.m.:
    Testing,
    focusing on the idea of tests as a way to specify what a program is supposed to do,
    and how to to structure unit tests using an xUnit-style library.
  * Day 2 p.m.:
    Number crunching using NumPy (depending on the audience).
* Common variations:
  * Command-line vs. IPython Notebook
    * Notebook can present install/config problems, and need to connect back to batch usage, but a nice teaching tool (esp. with embedded graphics, though hard to convince R users to take Python's matplotlib seriously)
    * Don't try to use a frozen notebook: code live!
  * R instead of Python
    * Some MATLAB lessons in the past, and certainly demand, but we're trying to be as open source as possible
  * Other version control systems (still some Subversion, some use Hg instead of Git)
  * Drop databases and do more Python (or cover plotting)
  * Some discussion of software lifecycles
  * Occasionally discussion of LaTeX
  * Not yet much domain-specific content, but as our instructor base grows, we're headed that way.
  * Multiple rooms (e.g., three-ring circus at U. Washington)
    * Don't shuffle people between rooms mid-way: too many dependencies

FIXME: we really want to teach the "how" of programming,
but people come for the "what".

Important:
we find workshops go a lot better if people come in groups
(e.g., 4-5 people from one lab, half a dozen from another department or institute, etc.)
so that they are less inhibited about asking questions
and can support each other afterward.
Also increases turnout from under-represented groups:
women, ESL, etc., are more likely to show up
if they know they're going to be among people they trust.
(Mention our code of conduct.)

A note on timing:
getting grad student at the start of their degrees is less effective
than getting them when they're far enough in to know that
they really, really need this.

Why not reproducibility?

* Assume five million scientific papers were published in the decade 1990-2000.
  (The actual number depends on what you include as a "paper", but our reasoning holds.)
* Of those, perhaps a hundred have been retracted because of honest computational irreproducibility
  ("honest", because fraud isn't part of this argument).
* That means the odds that a scientist will have to retract a particular paper because someone noticed that her calculations couldn't be reproduced are one in fifty thousand.
* So if the average paper takes eight months to produce,
  and scientists work six-day weeks,
  that means it's only worth spending 115 extra seconds per paper on reproducibility as insurance.

Different assumptions and models will naturally produce different answers,
but won't change the conclusion:
given the system we have today,
investing extra time to make work reproducible as insurance against error isn't economical.
RR's advocates may respond, "That's why we're trying to change the system,"
but chicken-and-egg traps are notoriously difficult to break out of:
if people don't care about the reproducibility of their own work,
they're unlikely to check it when reviewing other people's work, and around and around we go.
Trying to get them to be an early adopter of new practices
(which aren't yet rewarded consistently by their peer group)
is therefore a very hard sell.

This is more than just speculation.
When we first started teaching Software Carpentry at Los Alamos National Laboratory in 1998,
we talked a lot about the importance of testing to see if code was correct.
People nodded politely, but for the most part didn't actually change their working practices.
Once we started telling them that testing improved productivity by reducing re-work,
though,
we got significantly more uptake.
Why?
Because if you cut the time per paper (or other deliverable) from eight months to seven or six,
you've given people an immediate, tangible reward, regardless of what their peers may or may not do.

So here's my advice to advocates of reproducible research:
talk about how it helps the individual researcher get more done in less time.
Better yet,
measure that and publish the results.
Scientists have been trained to respect data;
if you can show them how much extra effort RR takes using today's tools,
versus how much re-work and rummaging around it saves,
they'll find your case much more compelling.

----

A couple of people have contacted us recently to ask about running Software Carpentry boot camps for companies.
Our material is all Creative Commons licensed,
so anyone who wants to use it for corporate training can do so, and doesn't need our permission.
What _does_ is using our name and logo,
since they're trademarked.
We're happy to give that permission if we've certified the instructor and have a chance to double-check the content.
(We've already had one instance of someone calling something "Software Carpentry" when it had nothing to do with what we usually teach.
We've worked hard to create material that actually helps scientists,
and to build some name recognition around it,
and we'd like to make sure our name continues to mean something.).
It would be great if starving grad students could help pay their bills from this,
in the way that many programmers earn part or all of their living from open source software.

## What Makes Us Different

The big idea that ties all of this together isn't actually the Unix philosophy;
it's that programming is a human activity.

* Short-term memory can only hold so much at a time, so build things to fit into it.
 * We're most productive when we're not being interrupted (or interrupting ourselves), so use tools that support an interactive do-and-see flow.
 * People are fallible, so make defense in depth a habit (i.e., check your data, figure out how to test things before you write them, run regression tests, etc.).

----

* We keep looking for things we can throw away, rather than things we can add.
  A few well-chosen concepts,
  well illustrated,
  is much more useful to our audience than a pile of facts.
  * This is part of why these courses aren't offered by CS departments:
    everyting we teach is old enough to (a) work well and (b) no longer be publishable.
    Command-line history, tab completion, putting things in scripts:
    old had to some, rocket science to others.
* Boot camps are interactive and hands-on:
  we tell instructors that if learners haven't typed in the last 15 minutes,
  they're talking too much.
* No slides!
  Live coding lets learners see how people grow programs
  (which is very hard to capture in video).
  Also encourages instructors to follow learners' lead,
  and not to go too long without breaks.
* They are peer-taught.
  Our instructors are scientists
  (many of whom have gone through boot camps themselves in the recent past),
  so the focus is very much "how does this improve research productivity"
  rather than "hey, here's some cool programming tools".
  * We don't promote software development skills, techniques and tools
    as being essential because software developers use them and so the
    attendees should too. Rather, understand what motivates the
    attendees and promote how these skills, techniques and tools
    address these motivations (e.g. scripting -> automation -> less
    mistakes + free up time for research, or testing -> spot mistakes
    in code -> prevent errors being introduced into your vital data)
    etc.
* We show people how the pieces fit together:
  how to write a Python script that fits into a Unix pipeline,
  how to automate their unit tests,
  etc.
* Focus on the carpentry level rather than engineering (explain the metaphor).
  * More appropriate for most scientists
  * More approachable too
* We are as open as we can be: grant proposals, feedback, etc., are all there.
  The fact that people can see us actively succeeding, failing, and learning
  buys us some credibility and respect.
* Our learners are highly motivated.
  They never _have_ to be there,
  and they're usually highly motivated.
* We eat our own cooking,
  e.g.,
  use GitHub ourselves for the web site, course materials, etc.
* We come to the learners, not vice versa.
  E.g., we continue to support all three major platforms,
  even though it's a lot more work for us.
* Etherpad!
  Don't ask student's to copy long URLs from your presentation to their computers.
* Sticky notes!
  Simple but effective teaching practice.
* Pair programming!
  A good practice in real life, a great way to teach.
* Starting with plain text files is good (easy to check correctness).
  * IPythonBlocks is another good tool (explain)
* Public good/bad feedback after every bootcamp
* Trying to base our teaching on empirical research:
  * What we know about learning and teaching (in general, and shout out to Guzdial)
  * What we know about software engineering

## Instructor Training

FIXME: write about the training course.

Why do people become instructors?

* _Make the world a better place._ As I say in a lot of my talks, the two things we need to get through the next hundred years are more science and more courage.  I don't know if we can do much about the latter, but we can sure help a lot with the former.
* _Make their own lives better._ Most of the time, we try to have astronomers teach astronomers, ecologists teach ecologists, and so on.  These are people whose tools instructors might one day want to use themselves, so by making them more clueful, instructors are helping themselves.
* _It's fun._  How could it not be?  You get to stand up and look smart in front of a bunch of smart people who actually want to be there, and you don't have to mark anything afterward.
* _Build a reputation._  Showing up to run a really useful workshop is a great way for people to introduce themselves to places they'd eventually like to work, and a great way to make contact with potential collaborators.  This is probably the most important reason from Software Carpentry's point of view, since it's what makes our model sustainable.
* _Get practice teaching._  We're doing more every year to train instructors, and giving them chances to teach online as well&mdash;both of which are useful for people with academic careers in mind.
* _Help get people of diverse backgrounds into the pipeline._ Computer Science is 12-15% female, and that figure has been _dropping_ since the 1980s.  From what I've seen, there's a similar gender skew among computationally-oriented people in other sciences, which if left alone will be self-perpetuating.  Some of our instructors are involved in part because they want to break that cycle and be a public example of a competent, confident woman programmer.
* _Teaching forces you to learn new things, or learn old things in more detail than you already know._ See for example "<a href="http://www.sciencemag.org/content/333/6045/1037.abstract">Graduate Students' Teaching Experiences Improve Their Methodological Research Skills</a>"
* _The more you know, the less you have to write yourself._ Putting a grant application together? Have a site review coming up?  We probably have slides for that... :-)

----

Jeffrey Mirel and Simona Goldin's recent article in <em>The Atlantic</em> titled "<a href="http://www.theatlantic.com/national/archive/2012/04/alone-in-the-classroom-why-teachers-are-too-isolated/255976/">Alone in the Classroom</a>" initially struck a chord with me, particularly when they said, "A recent study by Scholastic and the Gates Foundation found that teachers spend only about 3 percent of their teaching day collaborating with colleagues. The majority of American teachers plan, teach, and examine their practice alone." But then Mirel and Goldin blew it by saying:

>    So what would it take structurally to enable teachers to work collaboratively for improved learning outcomes?
>
>    Perhaps the most important change is in school curricula.
>    One of the key differences between public education in the U.S. and elsewhere is the lack of a common curriculum.
>    In other countries common curricula unite the work of teachers, school leaders, teacher educators, students, and parents.
>    With a common curriculum there is agreement about what students are expected to learn,
>    what teachers are to teach,
>    what teacher educators are to instill in potential teachers,
>    and what tests of student learning should measure.
>
>    A common curriculum for the nearly 100,000 K-12 schools in the U.S. could be a major step towards productive teacher collaboration.

No---a common curriculum won't improve teaching, and the things that _will_ don't need a common curriculum.
To understand why, have a look at another article in _The Atlantic_ from last December titled,
"<a href="http://www.theatlantic.com/national/archive/2011/12/what-americans-keep-ignoring-about-finlands-school-success/250564/">What Americans Keep Ignoring About Finland's School Success</a>",
which is based in part on Pasi Sahlberg's book <a href="http://www.amazon.com/Finnish-Lessons-Educational-Change-Finland/dp/0807752576/">_Finnish Lessons_</a>.
Sahlberg and others believe that the key to Finland's success are
(a) the fact that teachers are respected as professionals in a way they no longer are in North America,
and
(b) the fact that when they say, "No child will be left behind," they actually mean it:

>    It is possible to create equality.
>    And perhaps even more important---as a challenge to the American way of thinking about education reform---Finland's experience shows that
>    it is possible to achieve excellence by focusing not on competition,
>    but on cooperation,
>    and not on choice,
>    but on equity.
>
>    The problem facing education in America isn't the ethnic diversity of the population but the economic inequality of society,
>    and this is precisely the problem that Finnish education reform addressed.
>    More equity at home might just be what America needs to be more competitive abroad.

The question of how much commonality in the curriculum should be enforced vs. how much freedom instructors should have to adapt to local needs
is clearly relevant to Software Carpentry,
particularly when we start thinking about standards for responsible conduct of computational research.
More important, I think, are the questions of professionalism and equity:
how do we develop a cadre of instructors who know what to teach,
and how to teach it,
and how do we level the computational playing field so that everyone doing research has a fair shot at acquiring and using these skills?

## What's Not Working

Getting people to record themselves solving tasks as a graduation exercise.

Diversity of backgrounds/skill levels is a killer:
only long-term solution is to split by level
(which we can start to do now that we have more instructors).
Problem is,
people have a hard time self-selecting;
currently trialing an assessment so that we can at least give instructors a heads-up.

Only now doing the long-term post follow-up to see what impact we've had.

Diversity of platforms / install headaches

After-the-bootcamp follow-up still isn't working

We take text editors for granted and we shouldn't.

Don't do a good job of testing _scientific_ software (nobody does), but hoping to fix that as we move to media-first.

We still don't have exercises right: not enough, not diverse enough, not the right levels (some people lost, some bored)
That said, we do a good job of spotting people who are bored and turning them into helpers.

Git vs. Subversion: but we really don't know (yet).
Not the only thing we don't know: see blog/2013/04/spreadsheets-retractions-and-bias.html about our biases.

Online office hours have been a bust.

When teaching Python we tend to spend too much time on syntax and
basic programming issues instead of focusing on the core SWC materials
(better programming skills for those who already know how to
program). Teaching a programming language from scratch makes much
harder to focus on good programming practices (even if you're teaching
proficient programmers).  On the other hand, items such as
version control and databases are quite straight to the point. They
are self contained and fit very well in a couple of hours of teaching
time. Plus: most people understand straight away how they can adopt
(or not) them in their own work.

Still sometimes dive into details...

We're not teaching the web, and we need to.

## Conclusions

* The future is here, it's just not equally accessible.
  * Hard to do many of the cool things people are excited about without basic computing skills.
  * Impossible to know what new things of your own are already done/easy/hard/impossible.
* Driver's license exam is one way forward, RCR is another.
* We need to teach the rest of the lifecycle (esp. data management and communication)
* Hardest part: getting the powers that be to care about this

I realized a couple of days ago that I'd never blogged about
what Software Carpentry needs to accomplish in order to change the practice of science fundamentally and permanently.
In a nutshell,
we need to convert a fifth of scientists to our way of thinking.
Once we do that,
the odds are better than 50-50 that every time someone sends a paper out for review,
at least one reviewer will ask hard questions about how the computational work was done.
I get that number by assuming:

    Number of Reviewers | Fraction of Papers
    2                   | 10%
    3                   | 40%
    4                   | 40%
    5                   | 10%

So means the probability that none of a paper's reviewers will ask the right questions is 46.5%.
It's a grossly simplistic model, but at least it gives us something to shoot for.

- Why we don't teach reproducible research (yet)
  - Scientists don't care (above) and the tools aren't ready (don't add enough value early enough)
- We don't know nearly enough about real scientific software dev cycles, good or bad (just a few point samples from the top end)
  - So the best we can do is give them the pieces out of which most people we know assemble their workflows
- Include sample pre-assessment?
- Include demographic survey
- Mention assessments (Libarkin and Aranda)

From Aranda:

>    More importantly, this assessment concludes that Software Carpentry instruction helps scientists eliminate these weaknesses.
>    The program increases participants' computational understanding, as measured by more than a two-fold (130%) improvement in test scores after the workshop.
>    The program also enhances their habits and routines, and leads them to adopt tools and techniques that are considered standard practice in the software industry.
>    As a result, participants express extremely high levels of satisfaction with their involvement in Software Carpentry
>    (85% learned what they hoped to learn; 95% would recommend the workshop to others).
>
>    While the outcome is largely positive, there are areas for improvement.
>    Two of note are the spread in expertise among participants and the barriers that they face to change their software practice.
>    The first problem leads to some participants feeling that the instruction is too advanced or too basic for them.
>    The second problem damages the impact of Software Carpentry instruction,
>    as participants learn valuable material,
>    but find that for other reasons they are unable to adopt the relevant tools and techniques.

----

According to recent research, <a href="http://www.economist.com/node/21554506">an absence of optimism plays a large role in keeping people trapped in poverty</a>:

>    This hopelessness manifests itself in many ways.
>    One is a sort of pathological conservatism,
>    where people forgo even feasible things with potentially large benefits for fear of losing the little they already possess.

The parallels with scientific computing practically jump off the page.

