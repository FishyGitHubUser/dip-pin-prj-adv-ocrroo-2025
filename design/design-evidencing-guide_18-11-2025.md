# Overview

As part of the project, you are required to evidence that you have **designed** an advanced user interface that is fit for purpose.

The following guide will help you ensure that you have met the evidencing requirements while ensuring that you can work in an agile/iterative way that is appropriate for the project and modern software development practices.

## Design Evidencing

Modern design approaches are lightweight and combine iterations with user feedback. This is in contrast to traditional design approaches that are heavy on documentation and require a lot of up-front work.

However, often we cannot access the user in the frequency that allows rapid iteration. One way to mitigate this is to develop personas and scenarios that represent the user and their goals. 

### Minimum Requirements

1. In your project repository, create a folder called `design`.
2. In the `design` folder, create a file called `persona.md` that describes a representative persona
3. Create a subfolder with any design artefacts you created: wireframes, sketches, mockups, etc.]
4. Create at least three github issues related to the design of the application:
   1. Tag each issue with ui-design
   2. Assign each issue to a team member (when  one is allocated)
   3. Include a user story in the format "As a [persona], I want to [goal], so that [reason]"
   4. Add any non-functional requirements as notes in the issue
5. Copy this document into your project and answer any relevant questions

## Personas

A persona is a fictional character that represents a user. It is a way to describe the user's goals, needs, and behaviors. They are focused on **empathy** and **understanding** the user, not demographics, and not a collection of features.

> Describe the key persona your team is focused on implementing the design. You can describe the persona in a file called `persona.md` in the `design` folder.
>


### Persona Template

This is an optional template for how to structure your persona:

```markdown
# Persona: [Persona Name]

## Background
Give the person's background - make sure we can understand their level of skills, knowledge, and experience.

## Goals
Why does this person use the application? What are they trying to achieve?

## Needs
What does this person need from the application? What are their pain points?

```

### Relevant issue

Link to an issue that covers a pain point relevant to the persona and explain why it is relevant.
> A particular pain point for the persona might be: [Issue 3 - Fix Navigation Bugs](https://github.com/FishyGitHubUser/dip-pin-prj-adv-ocrroo-2025/issues/3).
> 
> Currently, there are elements which are hard to navigate to, due to the poor HTML hierarchy, as well as persistent content which is likely deprecated. This is likely to cause a poor navigation experience for the user.  

### Validation

You will validate your design by meeting with a user representative: the product owner (in this case, your lecturer).

> ### Meeting 1 - held on: 
> - 18 Nov 2025 - 18/11/2025
> 
> ### Persona discussed: 
> - [Savvy Wombat]
> 
> ### Design artefacts reviewed: 
> - https://github.com/FishyGitHubUser/dip-pin-prj-adv-ocrroo-2025/commits/initial-site
> 
> ### Issues discussed:
> 
> #### Big Issues:
> - There are lots of unimplemented features
> - This adds clutter to the page which makes it slightly confusing
> 
> ##### Smaller Issues:
> - The unimplemented features
> 
> ### Feedback provided: 
> - Layout is minimal and neat
> - Navigating is fairly straightforward
> - It would make more sense to have the OCR button above the readout or output
> - It would be good to have some feedback on the screen for users who are not completely blind. 
> - It's great to see you've taken the user persona fully onboard when creating this UI though
> - The transcripts/captions show/hide is currently confusing. 
> - I look forward to seeing the rest of the features implied by this page.

##### What worked well

- Layout is minimal and neat
- Navigation is fairly straightforward
- Considering the user persona when creating the UI

##### What could be improved

- OCR button should be above the readout or output
- There should be feedback on screen for users who are not completely blind
- The transcript show/hide is confusing

##### What will you change before the next meeting

- Streamline the layout
- Fix navigation bugs
- Reorganise remaining UI elements

##### Were there any questions that needed to be discussed with the user

> **Q.** Are there any additional features that they want implemented, or are needed.
> 
> **A.** It would be great to have some kind of personalisation to feel like it's my tool.

> Additionally, you can view the simulated scenario in UX design [here](../design/ai_design-evidence.html).
> 

#### Lecturer's checklist (to be used by the lecturer)

- [X] Persona is well-defined
- [X] Persona is relevant to the application
- [X] Design artifacts are present and easy to follow
- [X] Design decisions are based on user needs and goals
- [X] Appropriate considerations of interaction patterns appropriate for the user
- **[N/A]** Efforts towards realizing at least one significant issue involving user interaction
- [X] Whole team engagement in the design process
