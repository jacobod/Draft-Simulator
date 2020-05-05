# Draft-Simulator
Simulation of American Football drafts in Python

## Motivation

As a NFL and general american sports fan, draft season is one of the highlights of the year.

Generally, I spend a lot of time reading sites like FiveThirtyEight and Football Outsiders for more analytics-based draft content.
One of the things I noticed was that many analytics-based mock draft or simulations lacked detail on methodology. 
While always good reads, I always end up wanting to know more about the methodology and assumptions.
Given this, I thought developing a simulator from scratch would be a fun project- that I can potentially run before's next year draft..

The idea is we want to simulate a draft, given specific team needs, preferences, front office traits, and player projections. 
This includes trades (up/down), 


## Challenges and Assumptions

There are a few challenges that will impact this project:

- Many stats that would be useful in simulations to project a player's NFL Projection, like Football Outsider's DYAR, is behind a paywall and inaccessible
- Determining team's preferences is difficult, if not impossible. Thus, if a team has a need for WR, and the choice is between a 6'2 possession vs a 5'10 speedster who grade out similarly, we don't have a clear way to express preferences, only needs.

Assumptions

- Teams generally act rationally. For example, a team won't select a QB in first round despite value unless its a need 
- Teams have different goals (on hot seat so optimize for short term vs picking a player who needs development with potentially larger payoff in 3 years) 
- Teams have different levels of competence (teams percieved needs different than actual, or willing to sacrifice value in trades or pick player too early)
- Teams act differently, some are more prone to trade up/down, some never trade, etc.
- We do not know how players will actually turn out, the draft score will represent what general experts think


## Structure

- Players: position, attributes, draft score, etc
- PlayerPool: queue of players
- Teams: perceived needs (in future want to base on roster scores), has frontOffice
- FrontOffice: management traits, including competency, trade tendencies, etc.
- Draft: draft order, player pool. Manages overall simulation and makes picks. 
- Pick: owner (team). Generates possible trades based on team needs and resources, makes pick and updates player pool

### Inspiration

- Football Outsiders
- NFL's analytics content (Cynthia Frelund's wins added model comes to mind)
- FiveThirtyEight's NFL content
- ProFootballFocus



## Disclamer

This project has no affiliation with the National Football League (NFL) or any other organization named. 
Work does not reflect anyone's opinion other than my own.
