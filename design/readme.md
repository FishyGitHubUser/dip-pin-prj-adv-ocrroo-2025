# Overview

Put your design documentation in this folder.
This should include rough notes from the familiarization phase.


## Persona

Write a brief persona of your user using design thinking. You can use the following template:

- **Name**: [Savvy Wombat]
- **Age**: [36]
- **Occupation**: [Unemployed, looking for work]
- **Location**: [Perth City WA]
- **Goals**: [Get a turtle, Learn to program professionally, Become a food influencer, Start a business]
- **Frustrations**: [Bad hair days, Lack of clear and accessible learning resources and technologies, Pickles]
- **Motivations**: [Wants to become a millionaire before 50, Determined to prove her place in society, Waking up to eggs and breakfast]
- **Technology**: [Solidworks 365, Fusion 360, Excel, Pycharm, Adobe, Draw.io]
- **Experience**: [Experience of the user]
- **Personality**: [Cheerfully looking forward to challenges and puzzles, Struggles to comprehend sarcasm]
- **Interests**: [Puzzles, Food and animals, Programming, Drawing snails]

Notice: This project focuses on assistive technology for people with disabilities. It is important to treat the topic with respect and sensitivity.

Consider:

- People are not defined by their disabilities.
- People with disabilities are not a homogeneous group.

Your persona should reflect the diversity of people with disabilities and their experiences.

## User Journey

What is the user journey? What are the steps the user takes to achieve their goals?

- **Step 1**: [Get turtle: Become a millionaire and buy a turtle, then take it around the world.]
- **Step 2**: [Learn to program professionally: Study at the most advanced facilities to get the best learning experience. Bonus points for having learning assistance programs!]
- **Step 3**: [Become a food influencer: Practice cooking and taking selfies with food after getting a high paying job to cover food costs...]
- **Step 4**: [Start a business: Start my own company based on knowledge attained at my new job in the tech industry.]

## UI Interaction Patterns

What are the UI interaction patterns you will use in your project?
> > - Navigating elements and app functionality should have **screen reader friendly** text that addresses its functionality.
> > 
> > Note: This is mandatory, but not always addressed to the level of detail required accessibility by standards.
>  
> > - There should be a **shortcuts** for almost all interactions a user can make with the interface. 
> >
> > Note: They may not be required if the element serves no purpose, or has yet to be implemented.  
>  
> > - Apps may have **built-in support for screen readers**, or activate system screen readers via commands.
> > 
> > Note: This is usually not seen in most apps, but could have the option to install OS-based screen readers directly in the app.
> 
> > - **Colour accessibility** is important for visually impaired users that may need additional contrast, or more distinct colour schemes.
> >
> > Note: Most big companies usually have support for this feature, but have it hidden under a multitude of dropdown menus.
> 
> > - **Text scaling** can also be used to reduce, or increase the text size. This is useful for addressing unique screen sizes, or visual impairments.
> > 
> > Note: When featured on a site, the scaling usually has a limited range that may not address the user's needs.

## AI Prompts

Write down any AI prompts you came up with after your first session
> 1. You are a professional web developer tuned for accessibility, analyse the core concepts of vision impaired accessibility then address the topics mentioned by analysing accessibility best practices. Take a break, then double-check your answers and ensure you have addressed everything required, finally using your understanding of accessibility, include more issues that have not been addressed yet.
> <br><br>
> 2. Using your previous answer, create a single pure HTML page that addresses all accessibility requirements previously mentioned, as well as the following requirements:
>  
> ```text
> [{
>     'title': 'intro page', 
>     'background': 'blurred', 
>     'info card': 'centred, brief app description, press any page to redirect page and open file explorer',
>     },{
>     'title': 'app page', 
>     'header': 'left side has settings icon', 
>     'body': [
>         'left side has a vertically aligned video player', 
>         'right side has video settings for speed and uploading video button with OCR text area below',
>     ], 
>     'footer': '',
>     'notes': 'redirects to this page after selecting a file using OS explorer', 
> }]
> ```
> 
> Ensure the website follows strict html syntax while meeting all requirements. You may add basic CSS if required.
> <br>
> 3. Compare ONLY the html code file to the accessibility analysis, in a table write down the issue and mark if the requirement was met, and add notes if there's anything that could be changed. Finally, what would you change or add to make it even more accessible.
> 
> ### View [ChatGPT conversation](https://chatgpt.com/share/691367e0-2128-8007-b586-7c14639a3460).