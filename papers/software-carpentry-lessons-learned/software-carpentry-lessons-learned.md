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
* W. Trevor King (Drexel University / wking@drexel.edu)
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
(Cook2012):

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
attendees are actually learning and applying at least some of what we taught;
quoting (Aranda2012):

> ...this assessment concludes that Software Carpentry instruction helps scientists eliminate these weaknesses.
> The program increases participants' computational understanding,
> as measured by more than a two-fold (130%) improvement in test scores after the workshop.
> The program also enhances their habits and routines,
> and leads them to adopt tools and techniques that are considered standard practice in the software industry.
> As a result,
> participants express extremely high levels of satisfaction with their involvement in Software Carpentry
> (85% learned what they hoped to learn; 95% would recommend the workshop to others).

However,
many still find it hard to turn learning into practice,
and several of our experiments---most notably our attempts to teach online---have been failures.

## From Red to Green

Some historical context will help explain
where and why we have succeeded and failed.

### Version 1: Red Light

In 1995-96,
Greg Wilson organized a series of articles titled,
"What Should Computer Scientists Teach to Physical Scientists and Engineers?"
(Wilson1996).
The articles grew out of the frustration he felt working with scientists
who wanted to parallelize complex programs
but didn't know how to modularize their code,
test it,
or track changes
(Wilson2006a)---in short,
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
(Wilson2006b).
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
(even though a significant minority of their students,
particularly those coming from non-CS backgrounds,
have no more experience of practical software development
than the average physicist).
However,
other departments believe that courses like this ought to be offered by Computer Science,
in the same way that Mathematics and Statistics departments routinely offer service courses.
In the absence of an institutional mechanism to offer credit courses at some inter-departmental level,
this course,
like many other interdisciplinary courses,
fell between two stools.

> _It Works Too Well_
>
> We have also found that what we teach simply isn't interesting to most computer scientists.
> They are interested in doing research to advance our understanding of the science of computing;
> things like command-line history,
> tab completion,
> and "select * from table" have been around too long,
> and work too well,
> to be publishable any longer.
> As long as universities reward research first,
> and supply teaching last,
> it is simply not in most computer scientists own best interests
> to offer this kind of course.

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

### Version 4: Orange Light

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

### Version 5: Green Light

With new support from the Sloan Foundation and Mozilla,
Software Carpentry restarted in January 2012.
This time,
the model was two-day boot camps
modeled on those pioneered by The Hacker Within,
a grassroots group of grad students helping grad students
at the University of Wisconsin - Madison.

Shortening the boot camps made it possible for more people to attend,
and increased the proportion of material they retained.
It also forced us to think much harder about what skills scientists really needed.
Out went object-oriented programming,
XML, Make, GUI construction, design patterns,
software development lifecycles,
and other equally-useful topics.
Instead,
we focused on a handful of key tools---the shell,
a version control system,
a scripting language,
and a unit testing framework---that allowed us to introduce key concepts
in a hands-on way.

Reaching more people also allowed us to recruit more instructors from boot camp participants,
which was essential for scaling.
Switching to a "host site pays travel expenses" model was equally important:
we still need funding for the coordinator positions
(one full-time at Mozilla,
one part-time covered jointly by Mozilla and a donation from Continuum,
and part of one staff member's time at the Software Sustainability Institute in the UK),
but all of our other costs now take care of themselves.

## What We Do

So what does a typical boot camp look like?

* _Day 1 a.m._: Introduction to Unix shell.
  We show participants a dozen basic commands,
  but the real aim is to introduce them to pipes,
  loops and history (to automate repetitive tasks),
  and the idea of scripting.
* _Day 1 p.m._:
  Version control for file sharing,
  collaboration,
  and reproducibility.
  We usually use Git and GitHub these days,
  but some groups teach Mercurial or Subversion.
  If time permits,
  we wrap up with something like
  a quick intro to regular expressions.
* _Day 2 a.m._:
  An introduction to Python,
  the real goal of which is to show them
  when and why to develop code as a set of comprehensible, reusable functions.
* _Day 2 p.m._:
  Testing,
  focusing on the idea of tests as a way to specify what a program is supposed to do,
  and how to to structure unit tests using an xUnit-style library.
  As discussed later,
  this is probably the weakest part of our standard curriculum.
* _Day 2 p.m._:
  Number crunching using NumPy,
  or some other "beyond mere programming" topic
  such as an introduction to databases and SQL.

As the comments on the bullets above suggest,
our real aim isn't to teach Python, Git, or any other specific tool:
it's to teach _computational competence_.
We can't do this in the abstract:
people won't show up for a hand-waving talk,
and even if they do,
they won't understand.
If we show them how to solve a specific problem with a specific tool,
though,
we can then lead into a larger discussion of
how scientists ought to develop, use, and curate software.

We also try hard to show people how the pieces fit together:
how to write a Python script that fits into a Unix pipeline,
how to automate their unit tests,
etc.
Doing this gives us a chance to reinforce ideas,
and also increases the odds of them being able to apply what they've learned
once the boot camp is over.

Of course,
there are a lot of local variations around the template outlined above.
Some instructors use the command-line Python interpreter,
but a growing number have adopted the [http://ipython.org/notebook.html](IPython Notebook).
There are occasional installation problems,
and instructors do need to remember to connect what they've shown
to command-line (batch) usage,
but it has proven to be an excellent teaching and learning environment.
Its only real shortcoming isn't its fault:
Python's plotting libraries simply aren't compelling
to people who've been spoiled by R...

And speaking of R,
we have now run several boot camps using it instead of Python,
and expect this number to grow.
While some people feel that using R instead of Python
is like using feet and pounds instead of the metric system,
it is the _lingua franca_ of statistical computing,
particularly in the life sciences.
A handful of boot camps also cover tools such as LaTeX,
or domain-specific topics such as audio file processing.
We hope to do more of the latter going forward
now that we have enough instructors to specialize.

We aim for 40 people per workshop,
though we have gone as small as 9
and as large as 120.
We do _not_ recommend going over 40 in a single room:
instead,
we try to arrange multiple rooms,
and multiple instructors,
so that every learner can receive some personal attention.
When we do this,
we try not to shuffle people from one room to another
between the first and second day:
with the best inter-instructor coordination in the world,
it still results in duplication,
missed topics,
and jokes that make no sense.

Our boot camps have traditionally been free,
but we are starting to use a $20 cover charge to discourage no-shows.
(We have had boot camps where only half of those who signed up actually attended,
which is demoralizing for instructors.)
Even when we treat this charge as a deposit,
and refund it to participants who attended both days,
we must be very careful not to trip over institutional rules
about commercial use of their space:
some universities will charge us hundreds or thousands of dollars per day
for using their classrooms
if any money changes hands at any point.

> _Commercial Offerings_
> 
> Our material is all Creative Commons licensed,
> so anyone who wants to use it for corporate training can do so
> without explicit permission from us.
> We encourage this:
> it would be great if graduate students could help pay their bills
> by sharing what they know,
> in the way that many programmers earn part or all of their living
> from working on open source software.
>
> What _does_ require permission is use of our name and logo,
> both of which are trademarked.
> We're happy to give that permission if we've certified the instructor
> and have a chance to double-check the content,
> but we do want a chance to check:
> we have had one instance of someone calling something "Software Carpentry"
> when it had nothing to do with what we usually teach.
> We've worked hard to create material that actually helps scientists,
> and to build some name recognition around it,
> and we'd like to make sure our name continues to mean something.

As well as insructors,
we rely local helpers
to wander the room and answer questions during practicals.
These helpers may be participants in previous boot camps
who are interested in becoming instructors,
grad students who've picked up some or all of this on their own,
or members of the local open source community;
where possible,
we aim to have at least one helper for every eight learners.

We find workshops go a lot better if people come in groups,
e.g.,
4-5 people from one lab,
half a dozen from another department or institute,
etc.
They are less inhibited about asking questions,
and can support each other
(morally and technically)
when the time comes to put what they've learned into practice
after the boot camp is over.
Group signups also yield
much higher turnout from groups that are otherwise often under-represented,
such as women and minority students,
since they know in advance that they will be in a supportive environment.

Other lessons include:

_Live coding_
:   We use live coding rather than slides:
    it's more convincing,
    it enables instructors to be more responsive to "what if?" questions,
    and it facilitates lateral knowledge transfer
    (i.e.,
    people learn more than we realized we were teaching them by watching us work).
    This does put more of a burden on instructors than a pre-packaged slide deck,
    but most find it more fun.
_Open everything_
:   Our grant proposals,
    mailing lists,
    feedback from boot camps,
    and everything else that isn't personally sensitive
    is out in the open.
    While we can't prove it,
    we believe that the fact that people can see us actively succeeding, failing, and learning
    buys us some credibility and respect.
_Open lessons_
:   This is an important special case of the previous point.
    Anyone who wants to use our lessons can take what we have,
    make changes,
    and offer those back by sending us a pull request on GitHub.
    A common workflow in the open source world,
    it is still foreign to most scientists and educators
    (not least because file formats like Excel and PowerPoint
    don't play nicely with version control).
    This "eat your own dogfood" approach to teaching
    is allowing us to scale more quickly and more cheaply
    than the centralized approaches being taken by many online education ventures.
_Use what we teach_
:   We also make a point of eating our own cooking,
    e.g.,
    we use GitHub for our web site and to plan boot camps.
    Again,
    this buys us credibility,
    and gives instructors a chance to do some hands-on practice
    with the things they're going to teach.
_Meet the learners on their own ground_
:   Learners tell us that
    it's important to them to leave the boot camp
    with their own working environment set up.
    We therefore continue to teach on all three major platforms
    (Linux, Mac OS X, and Windows),
    even though it would be simpler to require learners to use just one.
    We are experimenting with virtual machines on learners' machines or in the cloud
    to reduce installation problems,
    but those introduce problems of their own:
    older or smaller machines simply aren't fast enough,
    and again,
    it's important to many learners
    to leave with their machines set up.
_Collaborative note-taking_
:   We often use [http://etherpad.org](Etherpad)
    for collaborative note-taking
    and to share snippets of code and small data files with learners.
    (If nothing else,
    it saves us from having to ask students
    to copy long URLs from the presenter's screen to their computers.)
    It is almost always mentioned positively in post-workshop feedback,
    and several boot camp participants have started using it in their own teaching.
_Sticky notes and minute cards_
:   Giving each learner two sticky notes of different colors
    allows instructors to do quick true/false questions as they're teaching.
    It also allows real-time feedback during hands-on work:
    learners can put a green sticky on their laptop when they have something done,
    or a red sticky when they need help.
    We also use them as minute cards:
    before each break,
    learners take a minute to write
    one thing they've learned on the green sticky,
    and one thing they found confusing (or too fast or too slow) on the red sticky.
    It only takes a couple of minutes to collate these,
    and allows instructors to adjust to learners' interests and speed.
_Pair programming_
:   Pairing is a good practice in real life,
    and an even better way to teach:
    partners can not only help each other out during the practical,
    but clarify each other's misconceptions when the solution is presented,
    and discuss common research interests during breaks.
    To facilitate it,
    we strongly prefer flat seating to banked (theater-style) seating;
    this also makes it easier for helpers to reach learners who need assistance.

## Instructor Training

To help people teach,
we now run an [http://teaching.software-carpentry.org](online training course)
for would-be instructors.
It takes 2-4 hours/week of their time for 12-14 weeks
(depending on scheduling interruptions),
and introduces them to the basics of educational psychology,
instructional design,
and how these things apply to teaching programming.
It's necessarily very shallow,
but most participants report that they find the material interesting as well as useful.

So why do people volunteer as instructors?

_To make the world a better place._
:   The two things we need to get through the next hundred years are more science and more courage;
    by helping scientists do more in less time,
    we are helping with the former.
_To make their own lives better._
:   Most of the time, we try to have astronomers teach astronomers, ecologists teach ecologists, and so on.
    These are people whose tools instructors might one day want to use themselves,
    so by helping them,
    instructors are helping themselves.
_To build a reputation._
:   Showing up to run a workshop is a great way for people to introduce themselves
    to places they'd eventually like to work,
    and a great way to make contact with potential collaborators.
    This is probably the most important reason from Software Carpentry's point of view,
    since it's what makes our model sustainable.
_To practice teaching._
:   This is also important to people contemplating academic careers.
_To help get people of diverse backgrounds into the pipeline._
:   Computing is 12-15% female,
    and that figure has been _dropping_ since the 1980s.
    While figures on female participation in computational science are hard to come by,
    a simple head count shows the same gender skew.
    Some of our instructors are involved in part because
    they want to break that cycle.
_To learn new things, or learn old things in more detail._
:   Working alongside an instructor with more experience
    is a great way to learn more about the tools,
    as well as about teaching.
_It's fun._
:   Our instructors get to work with smart people who actually want to be  in the room,
    and don't have to mark anything afterward.
    It's a refreshing change from teaching undergraduate calculus...

## What's Not Working

We've learned a lot,
and we're doing a much better job of reaching and teaching people
than we did eighteen months ago,
but there are still many things we need to improve.

The biggest challenge we face is
the diversity of our learners' backgrounds and skill levels.
No matter what we teach,
and how fast or how slow we go,
20% or more of the room will be lost,
and there's a good chance that a different 20% will be bored.
The obvious solution,
now that we have enough instructors to implement it,
is to split people by level.
The problem with that is figuring out what their levels are:
if we ask them to assess themselves,
they regularly under- or over-estimate their knowledge,
while giving them a proficiency test
scares away the people we most want to help.

We are currently testing a short pre-assessment questionnaire
intended to give instructors a better idea of
what their audience knows (and doesn't know)
before each boot camp starts.
We hope that will lead to some reliable way to stream learners,
but short of one-to-one interviews,
we believe this problem will never go away.

Our other big challenge is a longer-term issue.
We believe we're helping scientists be more productive,
but we're only just starting to do
the long-term, quantitative follow-up needed to prove this.
This is only partly because of limited resources:
the fact is,
no one knows how to measure the productivity of programmers,
or the productivity of scientists,
and putting the two together doesn't make the unknowns cancel out.
Again,
we are developing post-assessments to find out
what people actually adopt after boot camps,
and whether they feel it has helped them,
but measuring actual impact is a much harder problem.

> _Git vs. Subversion_
>
> One of the reasons we need to do long-term follow-up is
> to find out for our own benefit
> whether we're teaching the right things the right way.
> For example,
> some of us believe that Subversion is significantly easier for novices to understand than Git
> because there are fewer places data can reside
> and fewer steps in its normal workflow.
> Others believe just as strongly that there is no difference,
> or that Git is actually easier to learn.
> While learnability isn't the only concern---the large social network
> centered around GitHub is a factor as well---we would obviously be able
> to make better decisions
> if we had some.

Our third challenge is that
getting software installed is often harder than using it.
This is a hard enough problem for experienced users,
but almost by definition our audience is _inexperienced_,
and our learners don't (yet) know about system paths,
environment variables,
the half-dozen places configuration files can lurk on a modern system,
and so on.
Combine that with two version of Mac OS X,
three of Windows,
and two oddball Linux installations,
and it's almost inevitable that
every time we introduce a new tool,
it won't work as expected (or at all)
for at least one person in the room.

> _Edit This_
>
> And while it may seem like a trivial thing,
> editing text is always harder than we expect.
> We don't want to encourage people to use naive editors like Notepad,
> and the two most popular legacy editors on Unix (Vi and Emacs)
> are both usability nightmares.
> We now recommend a collection of open and almost-open GUI editors,
> but it remains a stumbling block.

Challenge #4 is to move more of our teaching and follow-up online.
We have tried several approaches,
from MOOC-style online-only offerings
to webcast tutorials
and one-to-one online office hours via VoIP and desktop sharing.
In all cases,
turnout has been mediocre at the start
and dropped off rapidly.

Fifth on our list is the tension between
teaching the "what" and the "how" of programming.
When we teach a scripting language like Python,
we have to spend time up front on syntax,
which leaves us only limited time for
the development practices that we really want to focus on,
but which are hard to grasp in the abstract.
By comparison,
version control and databases are straightforward:
what you see is what you do is what you get.

We also don't as good a job as we would like teaching testing.
The mechanics of unit testing with an xUnit-style framework are straightforward,
and it's easy to come up with representative test cases
for things like reformatting data files,
but what should we tell scientists about testing the numerical parts of their applications?
Once we've covered floating-point roundoff
and the need to use "almost equal" instead of "exactly equal",
our learners quite reasonably ask,
"What should I use as a tolerance for my computation?"
Saying,
"One part in a million, just because," isn't satisfying...

Finally,
we try to make our teaching as interactive as possible,
but we still don't give learners hands-on exercises
as frequently as we should.
We also don't give them as diverse a range of exercises as we should,
and those that we do give
are often at the wrong level.
This is partly due to a lack of time,
but disorganization on our part is also a contributing factor.

## Conclusions

To paraphrase William Gibson,
the future is already here---it's just that
the skills needed to implement it aren't evenly distributed.
A small number of scientists can easily build
an application that scours the web for recently-published data,
launch a cloud computing node to compare it to home-grown data sets,
and push the result to a GitHub account;
others are still struggling to free their data from Excel
and figure out which of the nine backup versions of their paper
is the one they sent for publication.

The fact is,
it's hard for scientists to do the cool things
their colleagues are excited about without basic computing skills,
and impossible for them to know what other new things are possible.
Our ambition is to change that:
not just to make scientists more productive today,
but to allow them to be part of the changes
that are transforming science in front of our eyes.
If you would like to help,
we'd like to hear from you.

## Bibliography

Aranda2012: Jorge Aranda: Report on Software Carpentry. FIXME: need citation.

Cook2012: John D. Cook: "Moore's law squared".  http://www.johndcook.com/blog/2012/01/01/moores-law-squared/, viewed 2013-05-17.

Wilson1996: Gregory V. Wilson: "What Should Computer Scientists Teach to Physical Scientists and Engineers?" *IEEE Computational Science & Engineering*, Summer-Fall 1996.

Wilson2006a: Greg Wilson: "Where's the Real Bottleneck in Scientific Computing?" *American Scientist*, January-February 2006.

Wilson2006b: Greg Wilson: "Software Carpentry: Getting Scientists to Write Better Code by Making Them More Productive" *Computing in Science & Engineering*, November-December 2006.
