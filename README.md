##### This Repository is one my 3 currently active repos, these are the repositories I'm currently focused on.
# pyTime
A Python T&A client to interact with a remote database to keep track of what users have been doing, where they've been doing it and for how long.

### The Idea
Initially I started this as a way to make myself stick to a healthy routine in my final year of college. The Idea was that I would use it to sign in in the mornings, out for break, back in and then out when I wen't home. This way I would be able to track how long I've spent in college per week, which lectures/labs I have missed/attended, and generally enforce a strict routine to stick to in order to reach peak performance.

### The Evolution
My friend pointed out that it was basically a T&A system for my own personal use, so that made me realise the potential to make this a bigger project that I'd initially intended. Instead I decided to make a general use T&A client (and server), this way I would be able to use it for the reason I'd originally intended but also have a useful application left behind even after I've finished.

### How It Will Work
The plan is to have a client application that is small, lightweight and intuitive, userfriendly and portable. This way any device with an internet connection (and python application support) can use it. I plan to implement a way to configure where people are allowed sign in/out, this can easily be done by assiging a whitelist of specific static IPs the client must be connected to to sign in, or maybe even implementing a location tracker to ensure they're within a certain distance of where they should be before they can sign in, the IP based location seems more practical though, for now.

### It's Current State
Currently stored in this repository is effectively just a GUI template. I'm currently developing the server side of things separately and will probably merge them in the future, into one Repository, but I haven't decided yet.
