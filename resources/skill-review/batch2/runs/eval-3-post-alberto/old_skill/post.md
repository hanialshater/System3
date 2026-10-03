☕️ Coffee & Commute — Call Alberto

3 Oct 2026

In 1764 a Scottish minister called Thomas Reid wrote that we come with "a disposition to confide in the veracity of others, and to believe what they tell us." In children, he said, it is unlimited, until they meet with instances of deceit and falsehood.

Then they meet their siblings.

I've been carrying Reid around on the bus this week, because he spoils one of our favourite things.

First principles.

You know the speech. Don't reason by analogy. Strip the problem down to what you know is true and rebuild it from there. Question every assumption. Ask why five times. Don't trust the docs, read the source.

And honestly? It's good advice. Some of the best engineering I've seen came from someone who refused to accept "that's how it's done here" and went back to the physics, or the profiler, or the actual bytes on the wire. A lot of bad systems survive because nobody ever asks why. The first-principles person asks. They're usually the most annoying person in the design review and they're often right.

So let's try it.

Do penguins live in Italy?

From first principles. Go.

You could start with penguin biology, the Mediterranean climate, ocean currents, the history of zoos. You could build a beautiful argument. Or you could do what I would actually do, which is call Alberto, who lives in Rome.

"Alberto, do penguins live in Italy?"

He laughs.

And now I know more than I did five minutes ago. Not with certainty. Alberto could be wrong. An escaped penguin could be crossing Piazza Navona right now and ruining my example. But Alberto is there, he sees Rome every day, and I have a history with him. If he says "I don't know about all of Italy, but I've never seen one in Rome," even the edge of his knowledge is useful.

Testimony comes with metadata. Where was the person standing? How did they behave last time? Where does their competence stop?

Now look at your own week. How much of what you "know" did you derive? You didn't re-derive TCP. You didn't audit the 400 packages your last `npm install` pulled in. You believe the benchmark in the paper, the incident write-up from the other team, and the senior engineer who says "don't touch that service on Fridays."

Our industry even has a slogan for the limit of first principles: don't roll your own crypto. That sentence is pure testimony. It means: people smarter than you bled here, believe them. And we are right to.

Nobody builds knowledge from an empty field. We grow it upward from a face (the first person who said "hot, don't touch") then siblings, teachers, books, colleagues, Alberto. When a layer fails we fix that layer and keep the rest.

So why does "first principles" survive, when everyone who's ever shipped anything knows they're standing on a mountain of other people's claims?

I think because testimony is invisible when it works. Nobody thanks the plumbing. When Alberto is right, it feels like *I* knew. When a borrowed claim breaks, we remember the one time we should have checked, and the slogan gets louder. First principles takes the credit for every success and testimony takes the blame for every failure. Not a bad deal, if you're first principles.

Which brings me to the thing I actually work on.

A language model has read everything Alberto ever wrote, and every blog post disagreeing with him, and the Reddit thread where someone confidently misunderstood both. It got the library without the childhood. What it mostly doesn't have is the metadata: who was positioned to know, how they behaved before, where their competence stops. Everything arrives in the same polished English.

So when we tell people "don't trust the LLM, verify everything yourself", we're handing them the first-principles speech again. It doesn't scale for them either.

The practical turn, for those of us building agents: stop asking only "is this claim true?" and start asking the Alberto questions. Where did this come from? Who was standing close enough to see it? What happened last time we trusted this source, this tool, this skill file? Write that down next to the claim. A rule in a prompt with no history is just a confident stranger.

Now the knife.

You've just believed a guy on a bus about an eighteenth-century Scottish minister. Did you check the quote? Did you check that Reid was a minister?

(He was. I checked. You're taking my word for that too.)

People might reasonably trust me on ranking systems, because I've spent years on them. They should not carry that credibility over to Scottish philosophy just because the same mouth is talking.

I'm your Alberto this morning.

You should probably call someone else too.

---

This is adapted from Chapter 4 of *System 3*, a book I'm writing about agents, trust and what we're entitled to treat as known. [link]
