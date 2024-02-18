## How to run it
If you'd like to try `Bite G'Nite`, you can clone and try it in your local server!!

## Inspiration
The inspiration behind Bite GoodNite came from the common yet often overlooked problem of bug bites, which can range from mildly annoying to medically serious. We aimed to leverage technology to provide quick, accessible information about various bug bites, helping users to identify them and understand when medical attention might be necessary.

## What it does
Bite GoodNite uses computer vision to analyze images of bug bites uploaded by users. By comparing these images to a vast database of bug bite characteristics, the AI model can identify the type of bug bite and suggest immediate care or whether to seek professional medical advice. Beyond identification, Bite GoodNite distinguishes itself by also educating users about the insects responsible for these bites, emphasizing the role of various insects in our ecosystem and how they benefit our environment. This dual approach not only aids in the immediate identification and understanding of bug bites but also fosters a greater appreciation for the ecological importance of insects, promoting a more informed and environmentally conscious community.

## How we built it
We built Bite GoodNite by first compiling a dataset of bug bite images and their corresponding attributes. We then used Python and scikit-learn to train a computer vision model. The user interface was developed with basic web technologies, including HTML, CSS, and Flask, to allow users to easily upload images and receive instant feedback.

## Challenges we ran into
One of our main challenges was the steep learning curve associated with Flask and scikit-learn, as our team was not initially familiar with these technologies. Additionally, dedicating the past two days entirely to bringing our vision to life meant overcoming significant time constraints and learning to quickly troubleshoot and iterate on our model.

## Accomplishments that we're proud of
We are particularly proud of training an AI model despite our initial unfamiliarity with the necessary technologies. Managing to create a user-friendly interface that simplifies the process of identifying bug bites from just an image is another achievement we take pride in.

## What we learned
Through this project, we learned not only technical skills related to Python, HTML, and machine learning but also valuable lessons in teamwork, problem-solving, and managing time effectively under pressure. The experience has enriched our understanding of the practical applications of AI and computer vision in healthcare.

## What's next for Bite GoodNite
Moving forward, we plan to expand the database to include more types of bug bites and possibly related skin conditions. We also aim to improve the accuracy of the AI model through continuous learning and user feedback. 
