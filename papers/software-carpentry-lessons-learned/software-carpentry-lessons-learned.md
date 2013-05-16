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
* Online lecture notes aren't really useful: people want *lectures*.
* No Wikipedia effect: good lessons are narratives, not merely facts presented in sequence.
* An awkward fit at universities:
  * CS departments believe it's too easy (even though many of their grad students are no better at software dev than anyone else)
  * Other departments believe CS should offer it (it's clearly not chemistry)
  * And those departments won't make room: what do they take out?

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

## What We Do

So what does a typical boot camp look like?

* Two days, two instructors, helpers, forty people
  * As mentioned earlier,
    our instructors are all volunteers,
    so the only costs to host sites are travel and accommodation
    (and coffee, if they choose).
* Most boot camps are still free, but we are starting to use a $20 cover charge to discourage no-shows
  * Either we keep it, or we refund it to people who are there both days
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
  * R instead of Python
    * Some MATLAB lessons in the past, and certainly demand, but we're trying to be as open source as possible
  * Other version control systems (still some Subversion, some use Hg instead of Git)
  * Drop databases and do more Python (or cover plotting)
  * Some discussion of software lifecycles
  * Occasionally discussion of LaTeX
  * Not *yet* much domain-specific content, but as our instructor base grows, we're headed that way.

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

A note on timing:
getting grad student at the start of their degrees is less effective
than getting them when they're far enough in to know that
they really, really need this.

## What Makes Us Different

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
  They never *have* to be there,
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

## Instructor Training

FIXME: write about the training course.

## What's Not Working

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

We still don't have exercises right: not enough, not diverse enough, not the right levels (some people lost, some bored)
That said, we do a good job of spotting people who are bored and turning them into helpers.

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

## Conclusions

* The future is here, it's just not equally accessible.
  * Hard to do many of the cool things people are excited about without basic computing skills.
  * Impossible to know what new things of your own are already done/easy/hard/impossible.
* Driver's license exam is one way forward, RCR is another.
* Hardest part: getting the powers that be to care about this

