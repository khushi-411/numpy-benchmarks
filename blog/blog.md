## My Experience
First of all, I'd like to express my gratitude to the whole team for allowing me to be a part of such a great team. These days were completely life-changing months of my journey. My work was majorly focused on providing performance benchmarks to NumPy in realistic situations. The target was to show the world that NumPy is efficient in handling quasi real-life situations too.

The work was broadly divided majorly into the following categories:
### N-Body Problem
The N-Body problem is one of the most famous and universally accepted problems for benchmarking.
I was given this as a problem statement to work on the project. I started my work with a theoretical understanding of the problem. It was a fun learning part for me to connect the scientific part with the programming world. I implemented the N-Body problem in Python, C, and C++.

### Compiled Methods
This part was the most exciting part of the project. I got introduced to various compiled methods like Cython, Pythran Numba, Transonic. It was the first time when I got to know about accelerators. I visited their documentations, GitHub, and searched blogs of other popular blogs of compiled methods. I loved playing with them. I used to read the theory part, looked into the examples, and implemented it in my editor. It was a fun learning for me to get familiar with compiled methods. I implemented the jitted compilers of Pythran and Numba for benchmarking via transonic's support.

### Visualization
I used the Matplotlib library for visualizing the benchmarking results. I tried a variety of plots to verify which one of the plots suits the best. We conclude that the bar chart is best suitable for benchmarking. I implemented many plots, but those were not good to go. Other than the bar chart, I had a few more options like scatter plots, box plots, line charts, the combination of the scatter plots and line charts, etc. These plots either lacked clarity or were not capable of providing significant results. We finalized horizontally stacked bar charts.
Documentation

### Model Optimization
Model Optimization was one of the most interesting parts for me to work on. I like playing with codes. The main task was to ensure we are obtaining similar results in all the implemented algorithms. I revisited all the code I had implemented earlier. At this stage, I was able to find out errors in my code and had an idea to improve it. The final aim was to achieve the same results in each step at a minimal time. Steps I followed to attain it:
- Initially, I used to play around with the library functions to check out which library function gave the best results.
- I then turned my focus to reduce the number of loops. And I'll say heads off to the Vectorized Approach of the NumPy. It is a savior to every solution. NumPy achieved a speed of more than 10% than Python and equivalent speed to that of compiled methods like C++ and Numba.
- Now the only task was to verify whether we have the same results in all the cases. Initially, I wanted to make my code as small as possible used many NumPy to show the effectiveness of the NumPy functions, but this, in turn, led to a decrement in the readability of code and made my code more complex. I learned that the structure of the code should be made easier to understand for the end-user. The ultimate goal was to prove that NumPy performs well even without using its special functions.

### Other Technical Lessons
- **Benchmarking Environment**: I enjoy changing my OS and love to taste different environments. But it was totally new for me to isolate a certain number of CPU cores for accurate benchmarking results. I referred to the official documentation of pypref and visited more than ten blogs to understand the idea
- **Git**: Getting familiar with various git commands was one of the coolest things I became comfortable with while working on Quansight.

### Advice to the Beginners
- Getting Familiar with the importance of the project: I believe: 'To find joy in the work the most important task is to know, where it started from.' Read the previous discussions made and know the reason for the importance of your project. I started my work with its origin. I read the issue related to benchmarking, articles, and other related work. I visited benchmarking page of other libraries too to get the idea. Among which the micro-benchmarks of NumPy using ASV are the best. It's too lovely!
- Search Everything about your project in the first 3-4 days: At this part, you need to get familiar with all the possible dots of your project. Look into as many related works of your project and examine the positive and negative points of the proposed work. Now it's high time to give structure to your project. I was pretty much sure about my work. After getting familiar with the problem statement, I read various works related to benchmarking. Fewer of them were initialcontiditions.org, benchmarks game, Julia's micro-benchmarks there were a few more. I agree that it took more than 3 days for me to complete, but I learned certain life hacks, which I'm damn sure that I will implement in every project. Make sure not to dig deeper into the topic, first know the width, then dive into the depth and ensure that you are stumbling upon the subject-related topics.
- Start working: Here come the journey starts. The best way to express yourself is to present everything that you have completed. Ask doubts as much as you can. But make sure that you have spent quality time in it. I used to update my mentor Matti Picus each day about the progress of our work, I am so glad to get such a mentor who has been really very responsive and understanding.
- Learn to prioritize things and make connections (make sure to express yourself). I learned to make connections with people being in Quansight. It was my first professional experience. I realized that the world is completely different. I still remember my first presentation (near about 2 years back), I was not even able to speak up. I am pleased that within a few months I interacted with such great personalities in The Quansight. And I am pretty sure it will go on and on!

### My Next Step
Quansight has opened lots of great opportunities for me in the open-source world. I aim to make myself comfortable in resolving issues and bugs. In the nearby future, I am looking forward to contributing to other projects. It was one of the best learning experiences for me. 

### Acknowledgment
I'd like to acknowledge my mentor Matti Picus, who has been very understanding and responsive towards my queries. I'd also like to thank Ralf Gommers and Melissa Weber Mendonca for setting up internship shares and giving us cool ideas for the project. Thanks to Ralf again who mentored me in absence of my mentor. Special thanks to Kushashwa Ravi Shrimali and Kshitij Kalambarkar for explaining cool learning tricks and life hacks. Thanks to you'll! It was great interacting with you'll.
