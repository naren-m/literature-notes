---
layout: "default"
title: "Brian Kernighan interview"
tags:
  - cse
  - theory
  - programming
  - book
word_count: 18659
created: "2024-11-28T18:24:53.212539"
modified: "2024-11-28T18:24:53.212539"
backlinks:
  - title: "GraphTheory"
    url: "graphtheory/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "People"
    url: "/topics/people//"
---
# Brian Kernighan interview

## Details

- Podcast     : Lex Fridman
- Topic       : Unix, C, AWK, AMPL and Go Programming language
- Link        : <https://www.youtube.com/watch?v=O9upVbGSBFo>
- Host        : Lex Firdman
- Guest       : [Brian Kernighan](docs/people/brian-kernighan/index/)
- Guest creds :

## Notes

- *CTSS* Time sharing system
- *Multics* build on top of CTSS to make it better
- [AMPL](docs/ampl/index/)

-

Kernighan coined the term "Unix" and helped popularize Thompson's [Unix philosophy](docs/cse/coding/unix-philosophy/index/).[17] Kernighan is also known as a coiner of the expression "What You See Is All You Get" (WYSIAYG), which is a sarcastic variant of the original "What You See Is What You Get" (WYSIWYG).[18] Kernighan's term is used to indicate that WYSIWYG systems might throw away information in a document that could be useful in other contexts.

In 1972, Kernighan described memory management in strings using "hello" and "world", in the B programming language,[19] which became the iconic example we know today. Kernighan's original 1978 implementation of [Hello World](docs/cse/coding/hello-world/index/) was sold at The Algorithm Auction, the world's first auction of computer algorithms.

- Uses Sam built by Rob Pike
- Auto code ? build by Tony burk?. https://youtu.be/O9upVbGSBFo?t=2869
- Early 1950s mostly Assembly laguage was used
- Late 1950s started programming language
    - Fortran done by IBM Formula Translation
    - Cobal for bussiness
    - Algol
- [AMPL](docs/ampl/index/)
  - Mathematical expressions
  - Specification of models, in human readable program.
  - The AMPL Book. #book #programming
- He also worked on [GraphTheory](docs/graphtheory/index/)
  - Under what conditions P=NP ? https://youtu.be/O9upVbGSBFo?t=4716
    - [Jeff Dean](jeff-dean/) either P is or or N is 1.
- What is *Computational complexity Theory*
  - Tags: #theory #cse
- His thesis is on [GraphTheory](docs/graphtheory/index/) Graph partition.
- Book on AI thought process around 1960s *Computers and Thought* #book

## Unix was not open source

I think that's a mischaracterization in the sense it absolutely was not open source it was very definitely proprietary licensed but it was licensed freely to universities in source code form for many years and because of that generations of university students and their faculty people grew up knowing about Unix and there was enough expertise in the community that it then became possible for people to kind of go off in their own direction and build something that looked unix like the berkeley version of unix started with that licensed code and gradually picked up enough of its own code contributions notably from people like [Bill joy](docs/people/bill-joy/index/) that eventually it was able to become completely free of any TMT code now there was an enormous amount of legal jockeying around this that in the late early to late 80s Early 90s something like that and then not

## Transcript of the video extracted by [YoutubeTrascript](docs/youtubetrascript/index/)



the following is a conversation with
[Brian Kernighan](docs/people/brian-kernighan/index/) a professor of computer
science at Princeton University he was a
key figure in the computer science
community in the early *UNIX* days
alongside UNIX creators Ken Thompson and
[Dennis Ritchie](docs/dennis-ritchie/index/) he co-authored the C
programming language with [Dennis Ritchie](docs/dennis-ritchie/index/)
the creator of C and has written a lot
of books on programming computers and
life including the practice of
programming the goal programming
language and his latest UNIX a history
and a memoir he co-created *awk*  the text
processing language used by Linux folks
like myself he Co designed [AMPL](docs/ampl/index/) an
algebraic modeling language that I
personally love and have used a lot in
my life for large scale optimization I
think I can keep going for a long time
with his creations and accomplishments
which is funny because given all that
he's one of the most humble and kind
people I've spoken to on this podcast.

the patro is packed with sensors that track heart rate heart rate variability and respiratory rate showing it all on their app once you wake up plus if you have a partner you can control the temperature of each side of the bed I don't happen to have one but the a sleep app reminds me that I should probably get on that so ladies if a temperature controlled mattress isn't a good reason to apply I don't know what is the apps health metrics are amazing but the cooling alone is honestly worth the money as some of you know I don't always sleep but when I do I choose the a sleep pod Pro mattress check it out at a sleep calm slash flex to get $200 off this show is also sponsored by Ray con earbuds get them at buy rake on Comm slash flex they've quickly become a main
method of listening to podcasts
audiobooks and music when I run do the
push ups and pull ups that have begun to
hate at this point or just living life
in fact I often listen to brown noise
with these what I'm thinking deeply
about something it helps me focus the
mind they're super comfortable pair
easily great sound great bass six hours
of play time in fact for fun I have one
of the earbuds in now and I'm listening
to Europa by Santana probably one of my
favorite guitar songs it kind of makes
me feel like I'm in a music video so
they told me to say that a bunch of
celebrities use these like Snoop Dogg
Melissa Etheridge and cardi B I don't
even know cardi B is but her earbud game
is on point to mention celebrities
actually care about
I'm sure if Richard Fineman was still
with us he'd be listening to the Joe
Rogan experience with Rick on earbuds
get them at by Drake on comm / Lex
it's how they know I sent you and
increases the chance that he'll support
this podcast in the future so for all of
the sponsors click all the links it
really helps this podcast and now here's
my conversation with Brian Kernighan
started being developed fifty years ago
in me more than fifty years ago can you
tell the story like you're describing
your new book of how UNIX was created ha
if I couldn't remember that far back
well it was some while ago um so I think
the gist of it is that at Bell Labs and
in 1969 there were a group of people who
had just finished working on the multics
project which was itself falling on to
CTS s so we can go back sort of an
infinite regress in time but the CTS s
was a very very very nice time sharing
system was very nice to use I actually
used it as that summer I spent in
Cambridge in 1966 for was the hardware
there right so what's the operating
system what's the hardware there what's
the CTS look like so cts s looked like
kind of like a standard time sharing
system certainly at the time it was the
only time sharing if no let's go back to
the basic ok in the beginning was the
word and the word sign there was time
sharing systems yeah if we go back into
let's call it the 1950s and early 1960s
most computing was done on very big
computers physically big although not
terribly powerful by today's standards
that were maintained in very large rooms
and you used things like punch cards to
write programs on talk to him so you
would take a deck of cards write your
program on it send it over a counter
hand it to an operator and some while
later back would come something that
said oh you made a mistake and then
you'd recycle and so it's very very slow
so the idea of time sharing was that you
take basically that same computer but
connect to it with something that looked
like an electric typewriter they could
be a long distance away it could be
closed but fundamentally what the
operating system did was to give each
person who was connected to it and
wanting to do something a small slice of
time on to do a particular job so I
might be editing a file so I would be
typing and every time I hit a keystroke
the operating system would wake up and
said oh he typed character let me
remember that and then it go back to
doing something else would be going
around and around a group of
who were trying to get something done
giving each a small slice of time and
giving them each the illusion that they
pretty much hit the whole machine to
themselves and hence time sharing that
is sharing the computing time resource
of the computer among a number of people
who are doing it without the individual
people being aware that there's others
in a sense the illusion the feeling is
that you the machine is your own pretty
much that was the idea yes you had if it
were well done and if it were fast
enough and other people were doing too
much you did have the illusion that you
had the whole machine to yourself and it
was very much better than the punch card
model and so cts s the compatible time
sharing system was I think arguably the
first of these it was done I guess
technically 64 or something like that it
ran on an IBM 7090 for slightly modified
to have twice as much memory as the norm
it had two banks of 32 k words instead
of one so 32 K words yes where's this 36

bit so call it you know about a hundred
and fifty kilobytes times two so by
today's standards that's down in the
noise yeah at the time that was a lot of
memory and memory was expensive so C TSS
was just a wonderful environment to work
on it was done by the people that MIT
led by Fernando Corbett Oh of Cour be
who died just earlier this year and a
bunch of other folks and then so I spent
the summer of 66 working on that had a
great time met a lot of really nice
people and indirectly knew of people at
Bell Labs who were also working on a
follow-on to C TSS that was called
multics so multics was meant to be the
system that would do everything that C
TSS did but do it better for a larger
population that's all the usual stuff
now the actual time sharing the
scheduling how much what's the algorithm
that performs the scheduling what's that
look like how much magic is there what
are the metrics how does it all work in
the beginning so the answers I don't
have a clue I think the basic idea was
nothing more than who all wants to get
something done suppose things are very
in the middle of the night then I get
all the time that I want suppose that
you and I are contending at high noon
for something like that then probably
the simplest algorithm is a round robin
one that gives you a bit of time gives
me a bit of time and then we could adapt
to that like what are you trying to do
are you text editing or are you
compiling or something and we might
adjust the scheduler according to things
like that so okay so multics
was trying to just do some of the clean
it up a little bit well it was it was
meant to be much more than that so
multix was the multiplexed information
and computing service and it was meant
to be a very large thing we would
provide computing utility something that
where you could actually think of it as
just a plug in the wall service sort of
like cloud computing today yeah same
idea but 50 odd years earlier
and so what multix offered was a richer
operating system environment piece of
hardware that was better designed for
doing the kind of sharing of resources
and presumably lots of other things do
you think people at that time had the
dream of what cloud computing is
starting to become now which is
computing is everywhere that you can
just plug in almost no you know and you
never know how the magic works you just
kind of plug in add in your little
computation they need to perform and it
does it it was that the dream I don't
know where that was the dream I wasn't
part of it at that point remember I was
an intern first summer but my sense is
given that it was over 50 years ago yeah
they had that idea that it was an
information utility that it was
something where if you had a computing
task to do you could just go and do it
now I'm betting that they didn't have
the same view of computing for the
masses let's call it the idea that you
know your grandmother would be shopping
on Amazon I don't think that was part of
it but if your grandmother were a
programmer it might be very easy for her
to go and use this kind of utility what
was your dream of computers at that time
what did you see as the future of
computers could you have predicted what
computers are today that you sense Oh
short answer absolutely not I have no
clue I'm not sure I had a dream it was a
dream job in the sense
that I really enjoyed what I was doing I
was surrounded by really really nice
people Cambridge is a very fine city to
live in in the summer less so in the
winter when it snows but in the summer
it was a delightful time and so I really
enjoyed all of that stuff and I learned
things and I think the good fortune of
being there for summer led me then to
get a summer job at Bell Labs the
following summer and that was going to
useful for the future so this Bell Labs
is this magical legendary place so first
of all where is Bell Labs and can you
start talking about that journey towards
Unix at Bell Labs
yeah so Bell Labs is physically
scattered around at the time scattered
around New Jersey the primary location
was in a town called Murray Hill where a
location called Murray Hill is actually
then across the boundary between two
small towns in New Jersey called New
Providence and Berkeley Heights think of
it as about 15-20 miles straight west of
New York City and therefore but an hour
north of here and for instance and at
that time it had make up a number three
or four thousand people there many of
whom had PhDs and mostly doing physical
sciences chemistry physics materials
kinds of things but very strong math and
it rapidly growing interest in computing
as people realized you could do things
with computers that you might not have
been able to do before you could replace
labs with computers that had worked on
models of what was going on so that was
the essence of Bell Labs and again I
wasn't the permanent play there I was
that was another internship I got lucky
in internships I mean if you could just
linger in a little bit what was the what
was in the air there because some of
this is the number of Nobel Prizes the
number of touring Awards and just
legendary computer scientists that come
from their inventions including
developments including UNIX it's just is
unbelievable so is it was there
something special about that place oh I
think there was very definitely
something special I mentioned the number
of people's a very large number of
people very highly skilled
working in an environment where there
was always something interesting to work
on because the goal of Bell Labs which
was a small part of a TMT which provided
basically the country's phone service
the goal of a TMT was to provide service
for everybody and the goal of Bell Labs
was to try and make that service keep
getting better so improving service and
that meant doing research on a lot of
different things physical devices like
the transistor or fiber optical cables
or microwave systems all of these things
the labs worked on and it was kind of
just the beginning of real boom times in
computing as well is when I was there I
went there first in 66 so computing was
at that point fairly young and so people
were discovering that you could do lots
of things with computers
so how's Unix born so multix in spite of

having an enormous number of really good
ideas lots of good people working on it
fundamentally didn't live up at least in
the short run and I think ultimately
really ever to its goal of being this
information utility it was too expensive
and certainly what was promised was
delivered much too late and so in
roughly the beginning of 1969 Bell Labs
pulled out of the project the project at
that point had included MIT Bell Labs
and General Electric General Electric
made computers so General Electric was
the hardware operation so Bell Labs
realizing this wasn't going anywhere on
a time scale they cared about
pulled out his project and this left
several people with an acquired taste
for really really nice computing
environments but no computing
environment and so they started thinking
about what could you do if you're going
to design a new operating system that
would provide the same kind of
comfortable computing as cts s head but
also the facilities of something like
multics sort of brought forward and so
they did a lot of paper design stuff and
at the same time Ken Thompson found what
is characterized as a little-used pdp-7
where he started to do experiments with
file systems just how do you
store information on a computer in an
efficient way and then this famous story
that his wife went away to California
for three weeks taking their
one-year-old son and three weeks and he
sat down and wrote an operating system
which ultimately became Unix so software
productivity was good in those days
the PDP what's the PDP seven so it's a
piece of hardware yeah it's a piece of
part where it was one of our leading
machines made by Digital Equipment
Corporation Dec and it was a mini
computer so called
it had yeah I would have to look up the
numbers exactly but it had a very small
amount of memory maybe 16 K 16-bit words
or something like that relatively slow
probably not super expensive maybe again
making this up I'd have to look it up a
hundred thousand dollars or something
like that which is not super expensive
in the sious right it was expensive it
was enough that you and I probably
wouldn't be my white one but a modest
group of people could get together but
in any case in it came out if I recall
in 1964 so by 1969 it was getting a
little obsolete and that's why it was
little used if you can sort of comment
what do you think it's like to write an
operating system like that so that
process that Ken went through in three
weeks because you were I mean you're
part of that process you've contributed
a lot to UNIX his early development so
what do you think it takes to do that
first step that first kind of from
designed to a reality on the PDP well
let me correct one thing I had nothing
to do with it so I did not write it I
have never written operating system code
and so I don't know now an operating
system is simply code and this first one
wasn't very big but it's something that
lets you run processes of some that you
execute some kind of code that has been
written it lets you store information
for periods of time so that it doesn't
go away when you turn the power off or
reboot or something like that and
there's a kind of a core set of tools
that are technically not part of an
operating system but you probably need
them in this case Ken wrote an assembler
for
pdp-7 that worked he needed a text
editor so that he could actually create
text he had the file system stuff that
he had been working on and then the rest
of it was just a way to load things
executable code from the file system
into the memory give it control and then
recover control when it was finished or
in some other way
quit what was the code written in the
primarily the programming language was
it in assembly pdp-7 assembler that Ken created these things were assembly language until probably the call at 1973 or 74 something like that yeah forgive me if it's a dumb question but it feels like a daunting task to write any kind of complex system in assembly absolutely it feels like impossible to do any kind of what we think of a software engineering assembly is to work on a big picture I think it's hard it's been a long time since I wrote assembly language it is absolutely true that in some other language if you make a mistake nobody tells you there are no training wheels whatsoever and so stuff doesn't work now what and there's no the buggers well there could be debuggers but that's the same problem right how do you actually get something that will help you debug it so part of it is is an ability to see the big picture now these systems were not big in the sense of today's picture so the big picture was
in some sense more manageable I mean
then realistically there's an enormous
variation in the capabilities of
programmers and *Ken Thompson* who did
that first one is kind of the
singularity in my experience of
programmers with no disrespect to you or
even to me he's gonna die several
leagues removed I know there's levels
this is it's a it's a fascinating thing
that there are unique stars in
particular in the programming space and
in a particular time you know the time
matters to the timing of when that
person comes along and the a wife does
have to leave see like there's this
weird timing that happens that and then
all sudden something beautiful is
created I mean how does it make you feel
that there's a system I was created in
in three weeks or
maybe you can even say on a whim but not
really but of course quickly that is now
you could think of most of the computers
in the world run on a unix-like system
right well how do you ensure like if you
kind of zoom from the alien perspective
if you're just observing earth that all
sudden these computers took over the
world and they started from this little
initial seed of *Unix*
how does that make you feel it's quite
surprising and and and you asked earlier
but predictions the answer is no there's
no way you could predict that kind of
evolution and I don't know whether it
was inevitable or just a whole sequence
of blind luck I suspect more the latter
and so I look at it and think gee that's
kind of neat I think the real question
is what this can think about that
because he's the guy arguably from whom
it really came tremendous contributions
from [Dennis Ritchie](docs/dennis-ritchie/index/) and then others
around in that Bell Labs environment but
you know if you had to pick a single
person that would be can see if written
in you book
UNIX a history and a memoir are there
some memorable human stories funny or
profound from that time they just kind
of stand out oh there's a lot of them in
a sense and again it's a question if can
you resurrect them this memory fails but
I think part of it was that Bell Labs at
the time was was a very special kind of
place to work because there were a lot
of interesting people and the
environment was very very open and free
it was a very cooperative environment
very from the environment and so if you
had an interesting problem you go and
talk to somebody and they might help you
with the solution and and it was a kind
of a fun environment to in which people
did strange things and often tweaking
the bureaucracy in one way or another
the rebellious and in some kinds of ways
in some ways yeah absolutely I think
most people didn't take too kindly to
the bureaucracy and I'm sure the
bureaucracy put up with an enormous that
they didn't really want to so maybe to
linger on it a little bit you have a
sense of what the philosophy that
characterized
unix's the design not just the initial
but just carry through the years just
being there being around what's the
fundamental philosophy behind the system
I think one aspect the fundamental
philosophy was to provide an environment
that made it easy to write her easier
productive to write program so as men as
a programmer environment it wasn't meant
specifically as something to do some
other kind of job for example it was
used extensively for word processing but
it wasn't designed as a word processing
system it was used extensively for lab
control but it wasn't designed for that
it was used extensively as a front end
for big other systems big dumb systems
but it wasn't designed for that it was
meant to be an environment where it was
really easy to write programs that so
the programmers could be highly
productive and part of that was to be a
community and there's some observation
from [Dennis Ritchie](docs/dennis-ritchie/index/) I think at the end
of the book that says that and that from
his standpoint the real goal was to
create a community where people could
work as programmers on a system I think
in that sense certainly for many many
years it succeeded quite well at that
and part of that is the technical
aspects of because it made it really
easy to write programs people did write
interesting programs those programs
tended to be used by other programmers
and so it was kind of a virtuous circle
are of more and more stuff coming out
that was really good for programmers and
you're part of that community of
programmers so what was the like writing
programs on that early unix it was a
blast it really was you know I like to
program I'm not a terribly good
programmer but it was a lot of fun to
write code and in the early days there
was an enormous amount of what you would
today I suppose called low-hanging fruit
people hadn't done things before and
this was this new environment and the
the whole combination of nice tools and
very responsive system and tremendous
colleagues made it possible to write
code you could have an idea in the
morning you could do it and you know an
experiment with it you could have
something limping along that night or
the next day and people would react to
it and they would say oh that's
wonderful
but you're really screwed up here and
and the feedback Luke was then very very
short and tight and so a lot of things
got developed fairly quickly that in
many cases still exists today and I
think that was part of what made it fun
because programming itself is fun it's
puzzle solving in a variety of ways but
I think it's even more fun when you do
something that somebody else then uses
even if they whine about it not working
the fact that they used it is as part of
the reward mechanism and what was the
method of an interaction the
communication we need that feedback loop
I mean this is before the internet
certainly before the internet um it was
mostly physical right there you know
somebody would come into your office and
say something so these places are all
closed but like offices are nearby we're
really lively into interaction yeah yeah
no Bell Labs was fundamentally one giant
building and most of the people were
involved in this unique stuff we're in
two or three quarters and there was a
room
oh how big was it probably call it 50
feet by 50 feet make up a number of that
and which had some access to computers
there as well as in offices and people
hung out there and had a coffee machine
and so that there was a it was mostly
very physical we did use email of course
and but it was fundamentally all for a
long time all on one machine so there
was no need for internet it's
fascinating to think about what
computing would be today without Bell
Labs it seems so many the people being
in the vicinity of each other it's sort
of getting that quick feedback working
together there's so many brilliant
people I don't know where else that
could have existed in the world I've
been given how that came together what
yeah well how does that make you feel
that that's a little element of history
well I think that's very nice but in a
sense it's survivor bias and if it
hadn't happened at Bell Labs there were
other places that we're doing really
interesting work as well Xerox PARC is
perhaps most obvious one Xerox PARC
contributed enormous amount of good
material and Men anything
we take for granted today in the same
way came from Xerox PARC experience I
don't think they capitalized in the long
run as much their parent company was
perhaps not as lucky in capitalizing on
this who knows but that would that's
certainly another place where there was
a tremendous amount of influence there
were a lot of good university activities
MIT was obviously no slouch in this kind
of thing and and others as well so Unix
turned out to be open source because of
the various ways that AT&T operated and
sort of they had to it was the focus was
on telephones so well. I think that's a
mischaracterization in the sense it
absolutely was not open source
it was very definitely proprietary
licensed but it was licensed freely to
universities in source code form for
many years and because of that
generations of university students and
their faculty people grew up knowing
about Unix
and there was enough expertise in the
community that it then became possible
for people to kind of go off in their
own direction and build something that
looked unix like the berkeley version of
unix started with that licensed code and
gradually picked up enough of its own
code contributions notably from people
like Bill joy that eventually it was
able to become completely free of any
TMT code now there was an enormous
amount of legal jockeying around this
that in the late early to late 80s Early
90s something like that and then not

something that I guess the open source
movement might have started when Richard
Stallman started to think about this in
the late 80s and by 1991 when Torvalds
decided he was going to do a unix-like
operating system there was enough
expertise that in the community that
first he had a target he could see what
to do because the kind of the UNIX
system call interface and the tools and
so on were there and so he was able to
build
an operating system that at this point
when you say UNIX in many cases what
you're really thinking is Linux Linux
yeah but it's it's funny that from my
distant perception I felt that UNIX was
open-source without actually knowing it
but what you're really saying it was
just freely licensed so it was freely
licensed it felt open-source in a sense
because universities are not trying to
make money so there it felt open-source
in a sense that you can get access if
you wanted right and a very very very
large number of universities had the
license and they were able to talk to
all the other universities who had the
license and so technically not open
technically belonging day T&T
pragmatically pretty open and so there's
a ripple effect that all the faculty and
the students then I'll grew up and then
they went throughout the world and
permeated in that kind of way so what
kind of features do you think made for a
good operating system if you take the
lessons of Unix you said like you know
make it easy for programmers like that
seems to be an important one but also
UNIX turned out to be exceptionally
robust and efficient right so is that an
accident when you focus on the
programmer or is that a natural outcome
I think part of the reason for
efficiency was that it began on
extremely modest hardware very very very
tiny and so you couldn't get carried
away you couldn't do a lot of
complicated things because you just
didn't have the resources either
processor speed or memory and so that
enforced a certain minimal 'ti of
mechanisms and maybe a search for
generalizations so that you would find
one mechanism that's served for a lot of
different things rather than having lots
of different special cases I think the
file system and UNIX is a good example
of that file system interface in its
fundamental form is extremely
straightforward and that means that you
can write code very very effectively
from for the file system and then one of
those ideas and one of those
generalizations is that gee that file
system interface works for all kinds of
other things as
well and so in particular the idea of
reading and writing to devices is the
same as reading and writing to a disk
that has a file system and then that
gets carried further in other parts of
the world processes become in effect
files in a file system and the plan 9
operating system which came along I
guess in the late 80s or something like
that
took a lot of those ideas from the
original unix and tried to push the
generalization even further so that in
plan 9 a lot of different resources our
file systems they all share that
interface so that would be one example
we're finding the right model of how to
do something means that an awful lot of
things become simpler and it means
therefore that more people can do useful
interesting things with them without him
to think as hard about it so you said
you're not a very good programmer you're
the most modest human being ok but
you'll continue saying that I understand
how this works but you do radiate a sort
of love for programming so let me ask do
you think programming is more an art or
science there's a creativity or kind of
rigor I think it's some of each it's
some combination some of the art is
figuring out what it is that did you
really want to do what should that
program be what would make a good
program and that's some understanding of
what the task is what the people who
might use this program want and I think
that's that's art in many respects the
science part is trying to figure out how
to do it well and some of that is a real
computer science II stuff like what
algorithm should we use at some point
mostly in the sense of being careful to
use algorithms that will actually work
properly or scale properly avoiding
quadratic algorithms when a linear
algorithm should be the right thing that
got a more formal view of it
same thing for data structures but also
it's I think an engineering field as
well then engineering is not quite the
same as science because engineering
you're working with constraints you have
to figure out not only so what is a good
algorithm for the
kind of thing but what's the most
appropriate algorithm given the amount
of time we have to compute the amount of
time we have to program what's likely to
happen in the future with maintenance
who's gonna pick this up in the future
all of those kind of things that if
you're an engineer you get to worry
about whereas if you think of yourself
as a scientist well you can maybe push
them over their horizon in a way and if
you're an artist what's that so just on
your own personal level what's your
process like of writing a program say a
small and large sort of tinkering with
stuff you just start coding right away
and just kind of evolve iteratively with
a loose notion or do you plan and a
sheet of paper first and then kind of
design and this you know what they teach
you in the kind of software engineering
courses an undergrad or something like
that what's your process like it's
certainly much more the informal
incremental first I don't write big
programs at this point it's been a long
time since I wrote a program that weighs
more and then I call it a few hundred or
more lines something like that many of
the programs are right or experiments
for either something I'm curious about
or often for something that I want to
talk about in a class and so those
necessarily tend to be relatively small
a lot of the kind of code I write these
days tends to be for sort of exploratory
data analysis where I've got some
collection of data and I want to try and
figure out what on earth is going on in
it and for that those programs tend to
be very small sometimes you're not even
programming you're just using existing
tools like counting things or sometimes
you're writing awk scripts because two
or three lines will tell you something
about a piece of data and then when it
gets bigger well and I will probably
write something in Python because that
scales better up to call it a few
hundred lines or something like that and
it's been a long time since I wrote
programs that were much more than that
speaking of data exploration in awk
first what is awk so awk is a scripting
language that was done by myself el hijo
on Peter Weinberger we did that
originally in the late 70s it was a
language that was meant to make
really easy to do quick and dirty tasks
like counting things or selecting
interesting information from basically
all text files rearranging it in some
way or summarizing it runs the command
on each line of a file I mean there's uh
it's still exceptionally widely used
today oh absolutely yeah it's so simple
an elegant sort of the way to explore
data turns out you can just write a
script that does something seemingly
trivial on a single line and that giving
you that slice of the data somehow
reveals something fundamental about the
data you know that keeps that seems to
work
still yeah it's very good for that kind
of thing that's sort of what it was
meant for I think what we didn't
appreciate was that the model is
actually quite good for a lot of data
processing kinds of tasks and that it's
it's kept going as long as it has
because at this point it's over 40 years
old but it's still I think a useful tool
and well this is paternal interest I
guess but I think in terms of
programming languages you get the most
bang for the buck by learning awk and it
doesn't scale the big programs but it
does pretty pretty darn well on these
little things where you just want to see
all the something's in something so yeah
I find I probably write more awk than
anything so what what kind of stuff do
you love about arc like is there if you
can comment on sort of things that give
you joy when you can in a simple program
reveal something about it is there
something that stands out from
particular features I think it's mostly
the selection of default behaviors that
you sort of hinted at at a moment ago
what Octus is to read through a set of
files and then within each file it rich
through a each of the lines and then on
each of the lines it has a set of
patterns that it looks for that's your
arc program and if one of the patterns
matches there is a corresponding action
that you might perform and so it's kind
of a quadruply nested loop or something
like that um and that's all completely
automatic you don't have to say any
think about it you just write the
pattern in the action and then run the
data by it and and so that paradigm for
programming is very natural and
effective one and I think we captured
that reasonably well and lock and it
does other things for free as well it
splits the data into fields so that on
each line there feels separated by white
space or something and so it does that
for free you don't have to say anything
about it and it collects information it
goes along like what line are we on how
many fields are there on this line so
lots of things that just make it so that
a program which in another language
let's say Python would be 5 10 20 lines
in Arcis one or two lines and so because
it's one or two lines you can do it on
the shell you don't have to open up
another whole thing you can just do it
right there and the interaction with
Allah perfectly is there other shell
commands that you love over the years
like you really enjoy using don't major
does everything so grep is a kind of
what is it a simpler version of awk I
would say in some some sense yeah right
because what is grep so grep is it
basically searches the input for
particular patterns regular expressions
technically of a certain class and it
has that same paradigm that awk does
it's a pattern action thing it reads
through all the files and then all the
lines in each file but it has a single
pattern which is the regular expression
you're looking for and a single action
printed if it matches so it's a in that
sense it's a much simpler version and
you could write crap in Arcis as a
one-liner and I use grep probably more
than anything else at this point just
because it it's so convenient and
natural why do you think it's such a
powerful tool grab not why do you think
operating systems like Windows for
example don't have it sort of you can of
course I use which is amazing now
there's windows for linux like the which
you could basically use all the fun
stuff like all can graph and inside of
Windows but Windows naturally sort of in
the best part of the graphical interface
the simplicity
sort of searching through a bunch of
files and just popping up naturally
why don't you think that why do you
think that's unique to the UNIX and
Linux environment I don't know I it's
not strictly unique but it's certainly
focused there and I think some of its
the weight of history that Windows came
from ms-dos ms-dos was a pretty pathetic
operating system although common own and
you know unbounded lis large number of
machines but somewhere in roughly the
90s windows became a graphical system
and I think Microsoft spent a lot of
their energy on making that graphical
interface what it is and that's a
different model of computing it's a
model of computing that where you point
and click and sort of experiment with
menus it's a model of computing worked
right rather well for people who are not
programmers just want to get something
done whereas teaching something like the
command line to non-programmers turns
out just sometimes be an uphill struggle
and so I think Microsoft probably was
right and what they did now you
mentioned whistle or whatever it's
called that winix I wonder what spinasse
wsl is but I've never actually
pronounced the whistle I like it I got
no idea but there have been things like
that for longest cygwin for example
which is a wonderful collection of take
all your favorite tools from UNIX and
Linux and just make them work perfectly
on Windows and so that's a something
that's been going on for at least 20
years if not longer and I use that on my
one remaining Windows machine aw
routinely because it it's for if you're
doing something that is batch computing
command sudo for command-line that's the
right way to do it because the windows
equivalents are if nothing else not
familiar to me but I should I would
definitely recommend to people to if
they don't use cygwin to try whistle yes
I say I've been so excited that I could
use best ivy bash write scripts quickly
in in Windows it's changed my life
okay what's your perfect programming
setup what computer what operating
system want keyboard what editor yeah
perfect is too strong a word is way to
struggle read of what
by default I have a at this point a
13-inch MacBook Air which I used because
it's kind of a reasonable balance of the
various things I need I can carry it
around it's got enough computing
horsepower screens big enough to
keyboards okay and so I basically do
most of my computing on that um I have a
big iMac in my office that I use from
time to time as well especially when I
need a big screen but otherwise none
tends not to be used as much editor I

use mostly Sam which is an editor that
*Rob Pike* wrote long ago at Bell Labs his
did that sorry to interrupt it does that
precede VI posts it post dates both VI
and Emacs it is derived from Rob's

experience with Edie and VI on D that's

the original UNIX editor o dated
probably before you were born so what's
actually what's the history of editors
can you can you briefly this is your fan
I used Emacs I'm sorry to say so I'm
sorry to come out with that but what's
what's the kind of interplay there yeah
so in ancient ancient times like call it
the first time sharing systems going
back to what we're talking about there
were editors there was an editor on C
TSS that I don't even remember what it
was called al it might have been edit
where you could type text program text
and it would do something or other
document text if it's saved then I'd
save it you could edit it you know the
usual thing that you would get in an
editor and Ken Thompson wrote an editor
called QED which was very very powerful
but these were all totally a command
based they were not most or cursor based
because it was before mice and even
before cursors because they were running
on terminals that printed on paper okay
no no CRT type displays let alone LEDs
and so then when UNIX came along Ken
took QED and stripped way way way way
down
and that became an editor that he called
needy it was very simple but it was a
line oriented editor and so you you
could load a file and then you could
talk about the lines one through the
last line and you could you know print
ranges of lines you could add text you
could delete text you could change text
or you could do a substitute command
that would change things within a line
or within groups of lines they can work
on a parts of a file essentially yeah
you could work on any part of it the
whole thing whatever but it was entirely
command line based and it was entirely
on paper okay paper and that meant that
you've changed yeah right real paper and
so if you changed the line you had to
print that line using up another line of
paper to see what changed cause okay
yeah
so when thing when CRT displays came
along yeah then you could start to use
cursor control and you could sort of
move where you where on the screen in
without reprinting printing and one of
there were a number of editors there the
one that I was most familiar with and
still use is VI which was done by bill
joy and so that dates from probably the
late 70s as a guess and it took at full
advantage of the cursor controls I
suspected Emacs was roughly at the same
time but I don't know I've never
internalized Emacs so so I use at this
point I stopped using IDI always can I
use VI sometimes and I use Sam when I
can and Sam is available on most systems
it was it is available you have to
download it yourself from typically the
plan line operating system distribution
it's been maintained by people there and
so I'll get home tonight I'll try it
that's cool it's a it's a sound sounds
fasting all though my love is with Lisp
and Emacs have went into that hippie
world of
I think it's likes what religion where
you brought up with yes sir that's right
most of the actual programming I do is C
C++ and Python but my weird sort of yeah
my religious upbringing is unless so can
you take on the impossible task and give
a brief history of programming languages
from your perspective so I guess you
could say programming languages started
probably in what the late 40s or
something like that people used to
program computers by basically putting
in zeros and ones using something like
switches on a console and then or maybe

holes and paper tapes something like
that so extremely tedious awful whatever
and so I think the first programming
languages were relatively crude assembly
languages where people would basically
write a program that would convert
mnemonics like add a DD into whatever
the bit pattern was it corresponding to
an add instruction and they'd do the
clerical work of figuring out where
things were so you could put a name on a
location in a program and the assembler
would figure out where that corresponded
to when the thing was all put together
and dropped into memory and they were
early on and this would be the late 40s
and very early 50s there were assemblers
written for the various machines that
people used you may have seen in the
paper just a couple days ago Tony
Burkert died he did this thing in
Manchester called the called auto code a
language for China knew only by name but
it sounds like it was a flavor of
assembly language sort of a little
higher in some ways um and a replaced on
language that Alan Turing wrote which
you put in zeros and ones but you put in
an in backwards order because that was a
Hardware worked very tense right yeah
yeah that's right backwards so assembly
languages learn let's call at the early
1950s and so every different flavor of
computer has its own assembly language
so the EDSAC head hits in a manchester
head it and the IBM whatever 70 90 or
704 or whatever had hits and so on so
everybody had their own assembly like
when assembly languages have a
few commands addition subtraction then
branching of some kind if then that the
situation right they have exactly in
their simplest form at least one
instruction per or one assembly language
instruction per instruction in the
machine's repertoire and so you have to
know the Machine intimately to be able
to write programs in it and if you write
an assembly language program for one
kind of machine and then you say jeez
it's nice I'd like a different machine
start over okay so very bad and so what
happened in the late 50s was people
realize you could play this game again
and you could move up a level in writing
or creating languages that were closer
to the way the real people might think
about how to write code and we're I
guess arguably three or four at that
time period there was Fortran which came
from IBM which was formula translation
and to make it easy to do scientific and
engineering computation is not that
formula translation that's what I stood
for yeah I where's COBOL which is the
common business oriented language that
Grace Hopper and others worked on which
was named business kinds of tasks there
was a well which was mostly meant to
describe algorithmic computations I
guess you could argue basic was in there
somewhere I think it's just a little
later and so all of those moved the
level up and so they were closer to what
you and I might think of as we were
trying to write a program and they were
focused on different domains Fortran for
formula translation engineering
computations let's say COBOL for
business that kind of thing still used
today
Fortran probably oh yeah COBOL too but
the deal was that once you moved up that
level then you let's call it Fortran you
had a language that was not tied to a
particular kind of hardware because a
different compiler would compile for
different kind of hardware and that
meant two things
it meant you only had to write the
program once which is very important and
it meant that you could in fact if you
were a random engineer physicist
whatever you could write that program
yourself you didn't have to hire a
programmer to do it for you might not be
as good as you'd get through a
programmer but it was pretty good and so
it democratized and made much more
broadly available the ability to write
code
so it puts the power of programming to
the hands of people like you yeah
anybody who wants to who under to invest
some time in learning a programming
language and is not then tied to a
particular kind of computer and then in
the 70s you get system programming
languages of which C is the survivor and
what what a system programming language
learning programs that programming
languages that would take on the kinds
of things that would necessary to write
so-called system programs things like
text editors or assemblers or compilers
or operating systems themselves those
kinds of things
and fortunately feature-rich they have
to be able to do a lot of stuff a lot of
memory management access processes and
all that kind of stuff they a little
processing it's a different flavor what
they're doing they're much more in touch
with the actual machine in a but in a
positive way that is you can talk about
memory in a more controlled way you can
talk about the different data types that
the Machine supports and underway there
and more ways to structure and organize
data and so the system programming
languages there was a lot of effort in
that and call it the late 60s early 70s
C is I think the only real survivor of
that and then what happens after that
you get things like object-oriented
programming languages because as you
write programs in a language like C at
some point scale gets to you and it's
too hard to keep track of the pieces and
there's no guardrails or training wheels
or something like that to prevent you
from doing bad things
so C++ comes out of that tradition it's
and then it took off from there I mean
there's also a parallel slightly
parallel track with a little bit of
functional stuff with Lisp and so on but
I guess from that point is just an
explosion of languages it was a Java
story there's the JavaScript there's all
the stuff that the cool kids these days
are doing with rust and all that they
don't so what's to use you're you wrote
a book C programming language what and C
is probably one of the most important
languages in the history of programming
languages if you kind of look at impact
what do you think is the most elegant or
powerful part of see why did it survive
what did it have such a long-lasting
impact I think it found a sweet spot
that in of expressiveness so you can
rewrite things in a pretty natural way
and efficiency which was particularly
important when computers were not nearly
as powerful as they are today
again put yourself back 50 years almost
in terms of what computers could do
that's you know roughly four or five
generations decades of Moore's law right
so expressiveness and efficiency and I
don't know perhaps the environment that
it came with as well which was Unix so
it meant if you wrote a program it could
be used on all those computers that ran
UNIX and that was all of those computers
because they were all written in C in
that way it was UNIX the operating
system itself was portable as where all
the tools so it all worked together
again and one of these things work
things fit on each other in a positive
cycle what did it take to write sort of
a definitive book probably the
definitive book on all of programs like
it's more definitive to a particular
language than any other book on any
other language and did two really
powerful things which is popularized the
language and at least from my
perspective maybe you can correct me and
second is created a standard of how you
know the how this language is supposed
to be used and applied so what did it
take did you have those kinds of
ambitions in mind when we're working on
that some kind of joke no of course not
of the knacks it's an accident of timing
skill and just luck a lot of it is
clearly I timing was good
now Denison I wrote the book in 1977 I
miss ritchi yeah right and at that point
UNIX was starting to spread I don't know
how many there were but it would be
dozens to hundreds of UNIX systems um
and C was also available on other kinds
of computers that had nothing to do with
UNIX and so the language had some
potential and there were no other books

on C and
Bell Labs was really the only source
Ford and Dennis of course was
authoritative because it was his
language and he had written the
reference manual which is a marvelous
example of how to write a reference
manual really really very very well done
so I twisted his arm until he agreed to
write a book and then we wrote a book
and the virtue our advantage at least I
guess if going first is that then other
people have to follow you if they're
gonna do anything and I think it worked
well because Dennis's superb writer I
mean he really really did and that the
reference manual in that book is his
period I had nothing to do with that at
all so just crystal-clear prose and very
very well expressed
um and then he and I I wrote most of the
expository material and then he and I
sort of did the usual ping-pong game
back and forth hum refining it but I
spend a lot of time trying to find
examples that would sort of hang
together and they would tell people what
they might need to know at about the
right time that they should be thinking
about needing it and I'm not sure it
completely succeeded but it mostly
worked out fairly well what do you think
is the power of example I mean you're
you're the creator at least one of the
first people to do the hello world
program just like the example if aliens
discover our civilization hundreds of
years from now they'll probably hello
what other programs just like a half
broken robot communicating with them
with the hello world so what and that's
a representative example so what what do
you find powerful about examples but I
think a good example will tell you how
to do something and it will be
representative of you might not want to
do exactly that but you will want to do
something that's at least in that same
general vein and so a lot of the
examples in the C book were picked for
these very very simple straightforward
text processing problems that were
typical of UNIX I want to read input and
write it again there's a copy command I
want to read input and do something to
it and write it out again there's a grep
and so that kind of fine things that are
representative of what people want to do
and spell those out so that they can
then take those and see the the core
parts and modify them to their taste and
I think that a lot of programming books
that I don't look at programming books a
tremendous amount these days but when I
do a lot of don't do that they don't
give you examples that are both
realistic and something you might want
to do some of them are pure syntax
here's how you add three numbers well
come on I could figure that I would tell
me how I would get those three numbers
into the computer and how he would do
something useful with them and then how
I put them back out again neatly
formatted and especially if you follow
that example there is something magical
of doing something that feels useful
yeah right and I think it's the attempt
and it's absolutely not perfect but the
attempt in all cases was to get
something that was going to be either
directly useful or would be very
representative of useful things that a
programmer might want to do but within
that vein of fundamentally text
processing reading text doing something
writing text so you've also written a
book on go language I'd have to admit so
I worked at Google for a while and I've
never used go not you miss something
well I know I missed something for sure
I mean yeah so go and rust the two
languages that I hear very
spoken very highly of night which I
would like to try well there's a lot of
them there's Julia there's there's all
these incredible modern languages but if
you can comment before or maybe comments
on what do you find where does go stood
in this broad spectrum of languages and
also how do you yourself feel about this
wide range of powerful interesting
languages that you may never even get to
try to explore of time so I think so go
um go first comes from that same Bell
Labs tradition in part not exclusively
but two of the three creators Ken
Thompson and Rob Michael literally the
people yeah the people
and then with this very very useful
influence from the European School in
particular the club spirit influence of
through Robert Griesemer it was I guess
a second generation down student at ETH
and so that's an interesting combination
of things and so some ways go captures
the good parts of see it looks sort of
like see it's sometimes characterized to
see for the 21st century on the surface
it looks very very much like see but at
the same time it has some interesting
data structuring capabilities and then I
think the part that I would say is
particularly useful and again I'm not a
go expert in spite of co-authoring the
book about 90% of the work was done by
Alan Donovan and my co-author who is a
go expert but go provides a very nice

model of concurrency it's basically the
cooperating communicating sequential
processes that Tony Hoare set forth I
don't know 40-plus years ago and go
routines are to my mind a very natural
way to talk about parallel computation
and in the few experiments I've done
with them they're easy to write and
typically it's going to work and very
efficient as well so I think that's one
place where it go stands out at that
model of parallel computation it's very
very easy and nice just to comment on
that do you think c4 saw or the early
unique States foresaw threads and
massively parallel computation I would
guess not really I mean maybe it was
seen but not at the level where it was
something you had to do anything about
for a long time processors got faster
and then processors stopped getting
faster because of things like power
consumption and heat generation and so
what happened instead was that instead
of processors getting faster there
started to be more of them and that's
where that parallel thread stuff comes
in so if you can comment on the
the other languages is it break your
heart that you'll never get to explore
them of course how do you feel a lot of
the full variety it's not break my heart
but but I would love to be able to try
more of these languages the closest I've
come is in class that I often teach in
the spring here it's a programming class
and I often give I have one sort of
small example that I will write in as
many languages as I possibly can I've
got it in 20 on languages at this point
and and that's so I do a minimal
experiment with on language just to say
okay I have this trivial task which I
understand the task and it should it
takes 15 lines in awk and not much more
in a variety of other languages so how
big is it how fast does it run and what
pain did I go through to learn how to do
it and that's a it's like an Akita right

it's a very very very narrowly like that
so yeah but still it's a little sample
because you get to I think the hardest
step of the programming language is
probably the first step right so there
you're taking the first step yeah and
from my experience um with some
languages is very positive
like Lua a scripting language I'd never
used and I took my Britain little
program the program is a trivial
formatter it just takes in lines of text
of varying lengths and it puts them out
in lines that have no more than 60
characters on each line so think it was
just kind of the flow of process in a
browser or something so it's very short
program and um in Lua I downloaded Lua
and in an hour I had it working
never having written Lua in my life just
going with online documentation I did
the same thing in Scala which you can
think of as a flavor of Java equally
trivial I did it in Haskell it took me
several weeks but it did run like a
turtle and and I did it in Fortran 90

and it painful but it worked and I tried
it in rust and it took me several days
to get it working because the model of
memory manage
it was just a little unfamiliar to me
and the problem I had with rust and it's
back to what we were just talking about
I couldn't find good consistent
documentation on rust now this was
several years ago and I'm sure things
have stabilized but at the time
everything in the rust world seemed to
be changing rapidly and so you would
find what looked like a working example
and it wouldn't work
with the version of the language that I
had so it took longer than it should
have rust is a language I would like to
get back to but probably won't I think
one of the issues you have to have
something you want to do if you don't
have something that is the right
combination if I want to do it and yet I
have enough disposable time whatever to
make it worse than learning a new
language at the same time it's never
going to happen so what do you think
about another language of JavaScript
that's this well let me just sort of
comment on what I said when I was
brought up sort of JavaScript pasina's
the probably like the ugliest language
possible and yet it's quite arguably
quite possibly taking over not just the
fun in the back end of the internet but
possibly in the future taking over
everything because they've now learned
to make it very efficient yeah so what
do you think about this yeah well I
think you've captured it in a lot of
ways when it first came out javascript
was deemed to be fairly irregular in an
ugly language and certainly in the
academy if you said you were working on
javascript people would ridicule you it
was just not fit for academics to work
on I think a lot of that has evolved the
language itself has evolved and
certainly the technology of compiling it
is fantastically better than it was and
so in that sense it's a absolutely a
viable solution upon backends as well
it's the front-end used well I think
it's a pretty good language I've written
a modest amount of it and I've played
with JavaScript translators and things
like that I'm not a real expert and it's
hard to keep up even there with the new
things that come along with it um so I
don't know whether it will ever take
over the world I think not but it it's
certainly an important
language and worth knowing more about
theirs
this may be to get your comment on
something which javascript and actually
most languages of Python such a big part
of the experience of programming with
those languages includes libraries sort
of using building on top of the code
that other people have built I think
that's probably different from the
experience that we just talked about
from UNIX and C days when you're
building stuff from scratch what do you
think about this world of essentially
leveraging building up libraries on top
of each other and leveraging them yeah
that's a very perceptive kind of
question one of the reasons programming
was fun in the old days was that you
were really building it all yourself the
number of libraries you had to deal with
was quite small maybe it was printf or
the standard library or something like
that and that is not the case today and
if you want to do something in you
mentioned Python and JavaScript and
those are the two finding examples you
have to typically download a boatload of
other stuff and you have no idea what
you're getting absolutely nothing
I've been doing some playing with
machine learning over the last couple of
days and G something doesn't work well
you pip install this okay and down comes
another gazillion megabytes of something
and you have no idea what it was and if
you're lucky it works and if it doesn't
work you have no recourse there's
absolutely no way you could figure out
which in these thousand different
packages and I think it's worse in the
MPM NPM environment for JavaScript I
think there's less discipline less
control there and there's aspects of not
just not understanding how it works but
there's security issues is there Busta's
issues so you don't want to run a
nuclear power plant using JavaScript
essentially oh probably not so it's
speaking to the variety of languages do
you think that variety is good or do you
hope think that over time we should
converge towards one two three
programming languages that's you
mentioned to the bailout days when
people could sort of the community of it
and the more languages you have the more
you separate the communities is the Ruby
there's the Python community there's C++
community do you hope that there they'll
unite one day - just one or two
languages I certainly don't hope it I'd
not sure that that's right because I
honestly don't think there is one
language that will suffice for all the
programming needs of the world are there
too many at this point well arguably um
but I think if you look at the sort of
the distribution of how they are used
there's something called a dozen
languages that probably count for 95% of
all programming at this point and that
doesn't seem unreasonable and then
there's another well 2000 languages that
are still in use that nobody uses and or
at least don't use in any quantity but I
think new languages are a good idea in
many respects because they're often a
chance to explore an idea of how a
language might help I think that's one
of the positive things about functional
languages for example they're a
particularly good place where people
have explored ideas that at the time
didn't seem feasible but ultimately have
wound up as part of mainstream languages
as well let me just go back as early as
recursion Lisp and then follow forward
with functions as first-class citizens
and pattern based languages and gee I
don't know closures and just on and on
and on lambdas interesting ideas that
showed up first in let's call it broadly
the functional programming community and
then find their way into mainstream
languages yes it's a playground for
rebels yeah exactly and and so I think
the language is in the playground
themselves are probably not going to be
the mainstream at least for some welp
but the ideas that come from there are
invaluable so let's go to something that
when I found out recently so I known
that you've done a million things but
one of the things I wasn't aware of the
you had a role in ample and I before you
interrupt me by minimizing your role in
it but your hapless for minimizing
functions
yeah minimizing functions right exactly
I can't just say that the elegance and
abstraction power of an ample is
incredible all right when I first came
to it about ten years ago or so can you
describe what is the ample language sure
so ample is a language for mathematical
programming technical term think of it
as linear programming that is setting up
systems of linear equations that are
some sort of system of constraints so
that you have a bunch of things that
have to be less than this greater than
that or whatever and you're trying to
find a set of values for some decision
variables that will maximize or minimize
some objective function so it's it's a
way of solving a particular kind of
optimization problem a very formal sort
of optimization problem but one that's
exceptionally useful and it specifies so
there's objective function of
constraints and variables that become
separate from the data it operates on
right so the that kind of separation
allows you to you know put on different
hats won't put the Hat of an
optimization person and then put a
another hat of a data person and dance
back and forth and and also separate the
actual solvers the optimization systems
that do the solving then you can have
other people come to the table and then
build their solvers whether it's linear
or nonlinear
convex non convex that kind of stuff so
what is the do use may be in common how

you got into that world and what is a
beautiful or interesting idea to you
from the world of optimization sure so I
preface it by saying I'm absolutely not
an expert on this and most of the
important work in and
comes from my two partners in crime on
that Bob Fuhrer who was a professor of
and in the industrial engineering and
management science department at
Northwestern and my colleague at Bell
Labs Dave Gay who is a numerical
analysts an optimization person so the
deal is linear programming preface this
by saying linear program is the simplest
example of this so linear program is
taught in school is that you have a big
matrix which is always called a and you
say ax is less than or equal to B so B
is a set of constraints X is the
decision variables and a as to how the
decision variables are combined to set
up the various constraints so a as a
matrix and X and B your vectors and then
there's an objective function which is
just the sum of a bunch of X's and some
coefficients on them and yet that's the
thing you want to optimize the problem
is that in the real world that matrix a
is a very very very intricate very large
and very sparse matrix where the various
components of the model are distributed
among the coefficients in a way that is
totally on obvious to anybody and so
what you need is some way to express the
original model which you and I would
write you know we'd write mathematics on
the board and the sum of this is greater
than the sum of that kind of thing so
you need a language to write those kinds
of constraints and Bob for a long time
had been interested in modeling
languages languages that made it
possible to do this there was a modeling
language around called gams the general
algebraic modeling system but it looked
very much like Fortran was kind of
clunky
um and so Bob spent a sabbatical year at
Bell Labs in 1984 and he and wasn't in
the office across from me and it's
always geography and he and Dave Gay and
I started talking about this kind of
thing and he wanted to design a language
that would make it so that you could
take these algebraic specifications you
know summation signs over sets and that
you would write on the board and convert
them into basically this a matrix
and then pass that off to a solver which
is an entirely separate thing and so we
talked about the design if the language
I don't remember any of the details of
this now but it's kind of an obvious
thing you're just writing mathematical
expressions in a Fortran like sorry in
algebra but textual like language and I
wrote the first version of this ample
program my first C++ program and that's

written in C++ yep and so I did that
fairly quickly we wrote it was you know
3,000 lines or something so it wasn't
very big but it just sort of showed the
feasibility of it that you could
actually do something that was easy for
people to specify models and convert it
into something that a solver could work
with at the same time as you say that
model and the data are separate thing so
one model would then work with all kinds
of different data in the same way lots
of programs do the same thing but with
different data so one of the really nice
things is the the specification of the
models human just kind of like as you
say is human readable like I literally
I'm ever on stuff I work I I would send
it to colleagues that I'm pretty sure
never programmed just just to understand
what the optimization problem is I think
how hard is it to convert that you said
you there's a first prototype in C++ to
convert that into something that could
actually be used by the solver it's not
too bad because most of the solvers have
some mechanism that lets them import a
model in AI form it might be as simple
as the matrix itself in just some
representation or if you're doing things
that are not linear programming and
there may be some mechanism that you
provide things like functions to be
called
or other constraints on the model so so

all ample does is to generate that kind
of thing and then solver deals with all
the hard work and then when the solver
comes back with numbers and Vil converts
those back into your original form so
you know how much of each thing you
should be buying or making or shipping
or what
so we did that in 84 and I haven't had a
lot to do with it since except that we
wrote a couple of versions of a book on
which is one of the greatest books ever
written I love that book I don't know
why it's an excellent book but for wrote
most of it and so it's really really
well done he must be a dynamite teacher
and typeset in late Dec no no no are you
kidding I really like in the typography
so I don't know we did it with tear off
I don't even know what that is yeah
exactly
you could go I think of tear off is as a
predecessor to the tech family of things
it's a formatter that was done at Bell
Labs in this same period of the very
early 70s
oh that predates tech and things like
that plate mmm 5 to 10 years it was
nevertheless they just I'm going by
memories it was I remember it being
beautiful yeah it was nice outside of
UNIX Iago laying all the things we
talked about all the amazing work you've
done you've also done working graph
theory
let me ask this this crazy out there
question if you had to make a bet and I
had to force you to make a bet do you
think P equals NP the answer is no
although I've told that somebody asked
Jeff Dean if that was the what
conditions B would equal NP and he said
either P is 0 or n is 1 or vice versa
I've forgotten so but your intuition is

I haven't no I have no intuition but
I've got a lot of colleagues who've got
intuition and their betting is no that's
the popular that's the popular bet okay
so what is computational complexity
theory and do you think these kinds of
complexity classes especially as you've
taught in this modern world there are
still a useful way to understand the
hardness of problems I don't do that
stuff the last time I touched anything
to do with that was before it was
invented because I it's literally true I
did my PhD thesis on good for big on on
tape
you know absolutely before I I did this
in 1968 and I worked on graph
partitioning which is this question
you've got a graph that is a nodes and
edges kind of graph and the edges have
weights and you just want to divide the
nodes into two piles of equal size so
that the number of edges that goes from
one side to the other is as small as
possible and we he developed so that
problem is hard well as it turns out I
work with Shen Lin at Bell Labs on this
and we were never able to come up with
anything that was guaranteed to give the
right answer we came up with heuristics
that worked pretty darn well and I
peeled off some special cases for my
thesis but it was just hard and that was
just about the time that Steve Cooke was
showing that there were classes of
problems that appeared to be really hard
of witchcraft partitioning was one but
this my expertise such as it was totally
predates that development Oh interesting
so the the heuristic which now you're
who cares the two of years names for the
Traveling Salesman problem at for the
graph partitioning that was like how did
you you weren't even thinking in terms
of classes you're just trying to was no
such idea a heuristic that kind of does
the job pretty well you were trying to
find a something that did the job and
there was no nothing that you would call
let's say a closed-form or algorithmic
thing that would give you a guaranteed
right answer I mean compare graph
partitioning to max-flow min-cut or
something like that that's the same
problem except there's no constraint on
the number of nodes on one side or the
other of the cut and that means it's an
easy problem at least as I understand it
whereas the constraint that says the two
have to be constrained in size makes it
a hard problem yes so the Robert Frost
has that poem where you choose two paths
so what why did you is there another
alternate universe in which you pursued
the Don Knuth path of you know algorithm
designs and of not smart enough that's
smart enough for you're infinitely
modest but so you proceed you're kind of
love of programming
I mean when you look back to those I
mean just looking into that world does
that just seem like a distant world of
theoretical computer science then is it
fundamentally different from the world
of programming I don't know I mean
certainly in all series and as I just
didn't have the talent for it I when I
got here is a grad student to Princeton
and I started to think about research at
the end of my first year or something
like that I work briefly with John
Hopkins absolutely you know he mentioned
during award-winner it said her a great
guy and it became crystal clear I was
not cut out for this stuff period okay
and so I moved into things where I was
more cut out for it and that tended to
be things like writing programs and
ultimately writing books you've said
that in Toronto as an undergrad you did
a senior thesis or literature survey on
artificial intelligence this was 1964
correct what was the AI landscape ideas
dreams at that time I think that was one
of the well you've heard of AI winters
this is whatever the opposite was AI
summer or something there's one of these
things where people thought that boy we
could do anything with computers that
all these hard problems we could
computers will solve them they will do
machine translation they will play games
like chess that they will do mission you
know prove theorems in geometry there
are all kinds of examples like that
where people thought boy we could really
do those sorts of things um and you know
I I read the kool-aid in some times it's
a wonderful collection of papers called
computers and thought that was published
and about that era and people were very
optimistic and then of course it turned
out that what people thought was just a
few years down the pike was more than a
few years down the pike and some parts
of that are more or less now sort of
under control
I we finally do play games like go and
chess and so on better than then people
do but there are others on machine
translation is a lot better than it you
to be but that's 50 close to 60 years of
progress and a lot of evolution in
hardware and a tremendous amount more
data upon which you can build systems
that actually can learn from some of
that and and the the infrastructure to
support developers working together like
an open source moving the internet
period is also an empowering but what
lesson do you draw from that the
opposite of winter that optimism well I
guess the lesson is that in the short
run it's pretty easy to be too
pessimistic or maybe too optimistic and
in the long run you probably shouldn't
be too pessimist I'm not saying that
very well it reminds me of this remark
from Arthur Clarke science fiction
author who says you know when some
distinguished but elderly person says
that something is him is possible he's
probably right and if he says it's
impossible he's almost surely wrong but
you don't know what the time scale is at
time scale is good all right so what are
your thoughts on this new summer of AI
now in the work with machine learning in
your networks you've kind of mentioned
he started to try to explore and look
into this world that seems fundamentally
different from the world of heuristics
and algorithms like search that it's now
purely sort of trying to take huge
amounts of data and learn learn from
that data right programs from the data
no look I think it's it's very
interesting I am incredibly far from an
expert most of what I know I've learned
from my students and they're probably
disappointed in how little I've learned
from them but um I think it has
tremendous potential for certain kinds
of things in games is one where it
obviously has had an effect on some of
the others as well I think there's and
this is speaking from definitely not
expertise I think there are serious
problems in certain kinds of machine
learning learning at least because what
they're learning from is the data that
we give them and if the data we give
them has something wrong with it then
what they learn from it is probably
wrong too and the obvious thing is some
kind of bias in the
that the data has stuff in it like I
don't know women earned as good at men
as men at something okay that's just
flat wrong but if it's in the data
because of historical treatment then
that machine learning stuff will
propagate that and that is a serious
worry the the positive part of that is
what machine learning does is reveal the
bias in the data and puts a mirror to
our own society and in so doing helps us
remove the bite you know helps us work
on ourselves it's a mirror to ourselves
yeah that's an optimistic point of view
and if it works that way that would be
absolutely great and and what I don't
know is whether it does work that way or
whether the the you know the AI
mechanisms or machine learning
mechanisms reinforce and amplify things
that have been wrong in the past and I
don't know I but I think that's a
serious thing that we have to be
concerned about let me ask you another
question okay I know nobody knows but
what do you think it takes to build a
system of human level intelligence
that's been the dream from the 60s we
talk about games about language about
about image recognition but really the
dream is to create human level or
superhuman level intelligence what do
you think it takes to do that and are we
close
I haven't a clue and I don't know trying
to trick you into a hypothesis I mean
Turing talked about this in his paper on
machine intelligence back and she's in
early 50s or something like that and he
had the idea of the Turing test and I
don't know what the Turing test is I
don't know it's an interesting test at
least it's in some vague sense objective
whether you can read anything into the
conclusions is a different story
do you have worries concerns excitement

about the future of artificial
intelligence so there's a lot of people
for worried and you can speak broadly
than just artificial intelligence is
basically computing taking over the
world in various forms are you excited
by this future this possibility of
computing being everywhere
or are you worried it's some combination
of those I I think almost all
technologies over the long run are for
good but there's plenty of examples
where they haven't been good either over
a long run for some people or over a
short run um
and computing is one of those and AI
within it is gonna be one of those as
well but computing broadly I mean for
just a today example is privacy that um
the use of things like social media and
so on means that in the commercial
surveillance means that there's an
enormous amount more known about us by
people other you know businesses
government whatever then perhaps one
ought to feel comfortable with so that's
an example that's an example pause a

possible negative negative effect of
competing being everywhere it's a it's
an interesting one because it could also
be a positive leverage correctly there's
a big if there so I I you know I've I
have a deep interest in human psychology
and humans are seem to be very paranoid
about this data thing at a but that
varies depending on age group yes it
seems like the younger folks so it's
exciting to me to see what society looks
like fifty years from now that the
concerns of our privacy might be flipped
on their head based purely on human
psychology versus actual concerns or not
yeah what do you think about Moore's law
well you said a lot of stuff we've
talked you talked about what programming
languages in their design and their
ideas are come from the constraints and
the systems they operate and do you
think Moore's Law the the exponential
improvement of systems will continue
indefinitely there's there's mix of
opinions on that currently or do you
think do you think there will be do you
think there'll be a plateau
well the furball is answer there's no
exponential can go on forever you run
out of something
um just as we said timescale matters so
if it goes on long enough
that might be all I need yeah right
won't matter does uh so I don't know
we've seen places where Moore's law has
changed for example mentioned earlier
process processors don't get faster
anymore but you used that same growth of
you know building put more things in a
given area to grow them horizontally
instead of vertically as it were so you
can get more and more processors or
memory or whatever on the same chip is
that gonna run into a limitation
presumably because you know at some
point you get down to the individual
atoms and so you got to find some way
around that will we find some way around
that I don't know I just said that if I
say it I'll be wrong we will say I just
talked to Jim Keller and he says so he
actually describes he argues that the
Moore's law will continue for a long
long time because you mentioned the atom
we actually have I think a thousandfold
increase to a decrease in threaten
transistor size still possible before we
get to the quantum level so it's there's
still a lot of possibilities he thinks
he'll continue indefinitely which is an
interesting optimistic optimistic
viewpoint but how do you think the
programming languages will change for
this increase whether we hit a wall or
not what do you think do you think
there'll be a fundamental change in the
way programming languages are designed I
don't worry about that I think what will
happen is continuation of what we see in
some areas at least which is that more
programming will be done by programs
than by people and that more will be
done by sort of declarative rather than
procedural mechanisms where I say I want
this to happen you figure out how and
that is in many cases at this point
domain of specialized languages for
narrow domains but you can imagine that
broadening out and so I don't have to
say so much in so much detail some
collection of software let's call it
language
or programs or something we'll figure
out how to do what I want to do some
increased levels of abstraction yeah and
one day getting to the human level maybe
just use so you taught so teach of

course computers in our world here at
Princeton that introduces computing and
programming to non majors what just from
that experience what advice do you have
for people who don't know anything about
programming but I'm kind of curious
about this world or programming seems to
become more and more of a fundamental
skill that people need to be at least
the world yeah well I could recommend a
good book what's that for the course I
think this is one of these questions of
should everybody know how to program and
I think the answer is probably not but I
think everybody should at least
understand sort of what it is so that if
you say to somebody I'm a programmer
they have a notion of what that might be
or if you say this is a program or this
was decided by a computer running a
program that they have some vague
intuitive understanding and an accurate
understanding of what that might imply
so part of what I'm doing in this course
which is very definitely for
non-technical people I mean typical
person in it is a history or English
major try and explain how computers work
how they do their thing what programming
is how you write a program and how
computers talk to each other and what do
they do when they're talking to each
other and then I would say nobody very

rarely and does anybody in that course
go on to become a real serious
programmer but at least they've got a
somewhat better idea of what all this
stuff is about not just the programming
but the technology behind computers and
communications do they write up do they
try and write a program themselves oh
yeah yeah a very small amount I
introduced them to how machines work at
a level below high-level languages so we
have a kind of a toy machine and has a
very small repertoire dozen instructions
and they write trivial assembly language
program Wow that's okay
just if you were to give a flavor to
people of the programming world for the
competing world what what are the
examples it should go with so a little
bit of assembly to get a sense at the
lowest level of what the program is
really doing yeah there's I mean in some
sense there's no such thing as the
lowest level because you can keep going
down but that's the place where I drew
the line so the idea that computers have
a fairly small repertoire of very simple
instructions that they can do like add
and subtract and and branch and so on as
you mentioned earlier and that you can
write code at that level and it will get
things done and then you have the levels
of abstraction that we get with
higher-level languages like Fortran or C
or whatever and that makes it easier to
write the code and less dependent on
particular architectures and then we
talk about a lot of the different kinds
of programs that they use all the time
that they don't probably realize our
programs like they're running Mac OS on
their computers or maybe Windows and
they're downloading apps on their phones
and all of those things are programs
that are just what we just talked about
except at a grand scale it's easy to
forget that they're actual programs that
people program there's engineers they
wrote wrote those things yeah right and
so in a way I'm expecting them to make
an enormous conceptual leap from their 5
or 10 line toy assembly language thing
that adds two or three numbers to you
know something that is a browser on
their phone or whatever but but it's
really the same thing if you look at the
broad and broad strokes at history what
do you think the world like how do you
think the world change because of
computers it's hard to sometimes see the
big picture when you're in it you know
but I guess I'm asking if there's
something you've noticed over the years
that like you were mentioned the
students are more distracted looking at
their now there's a device to look at
right well I think computing has changed
its rendus amount and obviously but I
think one aspect of that is the way that
people interact with each other
both locally and faraway and when I was
you know the age of those kids making a
phone call to somewhere was a big deal
because it cost serious money and this
was in the 60s right and today people
don't make phone calls they send texts
or something like that so it there's a
up and down and what people do people
think nothing of having correspondence
regular meetings video whatever with
friends or family or whatever in any
other part of the world and they don't
think about that at all they and so
that's just the communication aspect of
it and do you think that brings us
closer together or does it make us do
this does it take us away from the
closeness of human human contact I think
it depends a lot on all kinds of things
so I trade mail with my brother and
sister in Canada much more often than I
used to talk to them on the phone
so probably every 2 or 3 days I get
something or send something to them
whereas 20 years ago I probably wouldn't
have talked to them on the phone nearly
as much so in that sense I that's
brought my brother and sister and I
closer together that's a good thing um I
watch the kids on campus and they're
mostly walking around with their heads
down fooling with their phones to the
point where I have to duck them yeah I
don't know that that has brought them
closer together in some ways there's
sociological research that says people
are in fact not as close together as
they used to be I don't know whether
that's really true but but I can see
potential downsides and kids where you
think come on wake up and smell the
coffee or whatever that's right but if
you look at again nobody can predict the
future but are you excited kind of touch
this a little bit with with AI but are
you excited by the future in the next 10
20 years the computing will bring you
viewer there when there was no computers
really and now computers are everywhere
all over the world and
Africa and Asia and just every every
person almost every person the wall has
a device so are you hopeful optimistic
about that future I it's mixed if the
truth be told I mean I think there are
some things about that that are good I
think there's the potential for people
to improve their lives all over the
place and that's obviously good and at
the same time at least in the short time
short-run you can see lots and lots of
bad as people become more tribalistic
or parochial in their interests and it's
an enormous amount more us and them and
people are using computers in all kinds
of ways to mislead or misrepresented or
flat-out lie about what's going on and
that is affecting politics locally and I
think everywhere in the world
yeah the the long-term effect on
political systems and so on it's who
knows knows indeed the the the people

now have a voice which is a powerful
thing people who are press have a voice
but also everybody has a voice and the
chaos that emerges from that is
fascinating to watch yeah yeah it's kind
of scary if you can go back and relive a
moment in your life one that made you
truly happy outside of family or was
profoundly transformative is there a
moment or moments that jump out at you
from memory
I don't think specific moments I think
there were lots and lots and lots of
good times at Bell Labs where you would
build something and it it worked
hi Jase a work so the moments at war who
stood yeah and and somebody used it from
they said gee that's neat those kinds of
things happened quite often in that sort
of golden era and that the 70s when UNIX
was young and there was all this
low-hanging fruit and interesting things
to work on a group of people who kind of
we were all together in this and if you
did something they would try it out for
you and I think that was in some sense a
really really good time and Ock was a
was an example of that then you drilled
it and people use that yeah absolutely
and now millions of people use any and
all your stupid mistakes
right there for them to look at so it's
mixed
yeah it's terrifying vulnerable buds
beautiful because it does have a
positive impact on so so many people so
I think there's no better way to end it
Brian thank you so much for talking it
was an honor okay
likes it my pleasure good fun
thank you for listening to this
conversation with Brian Kernighan and
thank you to our sponsors 8:00 sleep
mattress and rake on earbuds please
consider supporting this podcast by
going to a sleep calm slash Lex and to
buy rake on comm slash Lex click the
links buy the stuff these both are
amazing products it really is the best
way to support this podcast and the
journey I'm on it's how they know I sent
you and increases the chance that
they'll actually support this podcast in
the future if you enjoy this thing
subscribe on youtube review it with fire
stars an apple podcast supported on
patreon or connect with me on Twitter at
Lex Freedman spelled somehow
miraculously without the letter e just
Fri D ma n because when we immigrated to
this country we were not so good at
spelling and now let me leave you with
some words from Brian Kernighan don't
comment bad code rewrite it
you for listening and hope to see you
next time

you
Get a transcript:
<https://www.youtube.com/watch?v=O9upVbGSBFo>
Reading is Faster
Blah blah welcome to my video begone!

Probably Won't Fail
Featuring the latest build of an undocumented API.

Easy to Use
Website definitely made with a bootstrap template.
