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

Over the last 15 years,
Software Carpentry has evolved into a worldwide volunteer effort
to raise standards in scientific computing.
This article explain what we have learned as we've grown,
and the challenges we now face.

## Introduction

In January 2012,
John Cook posted this to his widely-read blog
[cook2012][cook2012]:

> In a review of linear programming solvers from 1987 to 2002,
> Bob Bixby says that solvers benefited as much from algorithm improvements as from Moore's law:
> "Three orders of magnitude in machine speed
> and three orders of magnitude in algorithmic speed add up to six orders of magnitude in solving power.
> A model that might have taken a year to solve 10 years ago can now solve in less than 30 seconds."

A million-fold speedup is impressive,
but faster hardware and better algorithms are only two sides to the iron triangle of programming.
The third is programming itself,
and while improvements to languages and tools have undoubtedly made software developers more productive since 1987,
the speedup is measured in percentages,
not orders of magnitude.
Outwith the minority who do high-performance computing,
the time it takes the silent majority of scientists to produce a new computational result
is increasingly dominated by the time required to write, test, debug, install, and maintain software.

The problem is,
most scientists have never been taught how to do this.
Their undergraduate programs typically include either
a generic introduction to programming,
or a statistics or numerical methods course
in which they're expected to pick up programming on their own;
they are almost never told that version control exists,
and rarely if ever shown how to design a maintainable program in a systematic way,
or how to turn the last twenty commands they typed
into a re-usable script.
As a result,
they routinely spend hours doing things that could be done in minutes,
or failing to do things at all because they don't know where to start.

This is where Software Carpentry comes in.
We ran 92 two-day workshops between January 2012 and July 2013.
In them,
more than 100 people helped over 3000 scientists learn about
program design,
task automation,
version control,
testing,
and the other unglamorous but time-tested skills
that help scientists get more done in less time,
and have more confidence in their results.
Two independent assessments in 2012 showed that
attendees are actually learning and applying at least some of what we taught,
but many still find it hard to turn learning into practice,
and several of our experiments---most notably our attempts to teach online---have been failures.

## Red, Red, Orange, Green

Some historical context will help explain
where and why we have succeeded and failed.

### Version 1: Red Light

In 1995-96,
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
The course ran for the first time in July 1998;
after several re-starts during the next 12 years,
Software Carpentry began running two-day bootcamps
aimed primarily at graduate students
with at least a little prior programming experience.

The course eventually wound down as the principals moved on to other projects,
but several valuable lessons were learned:

1. Intensive week-long courses are easy to schedule (particularly if instructors are traveling)
   but by the end of the second day,
   attendees brains are full
   and learning drops off significantly.
2. Traditional software engineering is not the right thing to teach most scientists.
   In particular, careful documentation of requirements and lots of up-front design
   aren't appropriate to people who (almost by definition)
   don't yet know what they're trying to do.
   Agile development methods (which rose to prominence during this period) are less alien,
   but even those are unsuited to the "solo grad student" model of working
   which is so common in science.
   (After all,
   it's hard to pair program if no one else is working on your code...)

### Versions 2 and 3: Another Red Light

The Software Carpentry course materials
were updated and released under a Creative Commons license in 2004-05
thanks to support from the Python Software Foundation
[wilson2006b][wilson2006b].
They were then used twice in a conventional term-long graduate course
at the University of Toronto
aimed at a mix of students from Computer Science and the physical and life sciences.

The online materials,
which were written in point-form lecture slide style,
attracted 1000-2000 unique visitors/month
(with occasional spikes correlated to courses and mentions in other sites).
However:

1. Many potential users reported that online lecture notes weren't very useful on their own.
   As one said,
   they were sheet music,
   when what people wanted was a performance of the song
   (and even more,
   the ability to ask questions).
2. Despite repeated invitations,
   other people did not contribute updates or new material
   (other than the occasional bug report).
   We believe this is related to the previous point:
   good lessons are narratives,
   not merely facts presented in sequence,
   so editing a lesson is more akin to editing a story
   than to editing a Wikipedia entry.
3. While grad students (and the occasional faculty member) found the "live" course at Toronto useful,
   it never found a comfortable institutional home.

This last point deserves elaboration.
Most Computer Science faculty believe this basic material is too easy to deserve a graduate credit
(even though many of their students,
particularly those coming from non-CS backgrounds,
are no better at software development than anyone else).
However,
other departments believe that courses like this ought to be offered by Computer Science,
in the same way that Mathematics and Statistics departments routinely offer service courses.
In the absence of an institutional mechanism to offer credit courses at some inter-departmental level,
this course,
like many other interdisciplinary courses,
fell between two stools.

The most important lesson learned in this period,
though,
was even more fundamental.
Many faculty will agree that their students should learn more about computing.
What they _won't_ agree on is
what to take out of the current curriculum to make room for it.
A typical undergraduate chemistry degree has roughly 1800 hours of class and laboratory time;
anyone who wants to add more programming,
more statistics,
more writing,
or more of anything else
must either lengthen the program
or take something out.
However,
everything that's in the program is there because it has a passionate defender
who thinks it's vitally important.
Saying, "We'll just add a little computing to every other course," is a cheat:
five minutes per hour adds up to four entire courses in a four-year program.
Pushing computing down to the high school level is also a non-starter,
since that curriculum is also full.

The sweet spot for this kind of training is therefore
the first two or three years of graduate school.
At that point,
students have time
(at least, more time than they'll have once they're faculty)
and real problems of their own that they want to solve.

## Version 3: Orange Light

Wilson rebooted Software Carpentry in May 2010
with support from
Indiana University,
Michigan State University,
Microsoft,
MITACS,
Queen Mary University of London,
Scimatic,
SciNet,
SHARCNet,
and the UK Met Office.
More than 120 short video lessons were recorded during the following 12 months,
and six more week-long classes were run on-site for the backers.
We also offered an online class three times
(a MOOC _avant la lettre_).

This was our most successful version to date,
in part because the scientific landscape itself had changed.
Open access publishing,
crowd sourcing,
and dozens of other innovations had convinced scientists
that programming was now as unavoidable as statistics.
However,
most still regarded it is a tax they had to pay in order to get their science done;
while those of us who teach programming may find it interesting in its own right,
most of our audience clearly wants to learn as little as they have to
so that they can get back to the lab
and finish the paper whose deadline is looming.

Despite this round's success,
there were several disappointments:

1. Once again,
   we discovered that five eight-hour days are more wearying than enlightening.
2. And once again,
   only a handful of other people contributed material
   (Orion Buske, Tommy Guy, Jason Montojo, Jon Pipitone, and Ethan White).
   We believe this was in part because
   creating video lectures
   is even more challenging than creating slide-style lectures.
   Editing or modifying them is harder still:
   while a typo in a slide can be fixed by opening PowerPoint,
   making the change,
   saving,
   and re-exporting the PDF,
   inserting new slides into a video
   and updating the soundtrack
   seems to take at least half an hour
   regardless of how small the change is.
3. Most importantly,
   the MOOC format didn't work:
   only 5-10% of those who started with us finished,
   and the majority were people who already knew most of the material.
   Both figures are in line with completion rates and learner demographics for other MOOCs,
   but are no less disappointing because of that.

The biggest take-away from this round,
though,
was the need come up with a scalable, sustainable model.
One instructor simply can't reach enough people,
and cobbling together funding from half a dozen different sources
every twelve to eighteen months
is a high-risk approach.

## Version 4: Green Light

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

----

## Context: The Missing Side of the Triangle

Distinguish openness, reproducibility, and computational competence.

"It only takes a few minutes to show someone how to write a simple CGI script, or to tweak some PHP to modify a WordPress plugin."
Well, yes, but that's like saying that it only takes a few minutes to show someone how to start a car and get it out on the road.
It's what we have to teach people so that they can survive what happens next that takes time. 

----

## Bibliography

[cook2012] John D. Cook: "Moore's law squared".  http://www.johndcook.com/blog/2012/01/01/moores-law-squared/, viewed 2013-05-17.

  * For example, see blog/2012/12/computer-science-curricula-2013.html for a comparison with the ACM curriculum guidelines
