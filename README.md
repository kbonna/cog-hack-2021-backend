## Cog_HACK hackathon prooject

This repository contains backend Django code for Moodlist app created during Cog_HACK hackathon.

Moodlist app automatically detects emotion on user face and use that information to create personalized music playlist sutiable for a given mood.

Features:
  - REST API is used to send user image and respond with detected emotions
  - open source [fer](https://github.com/justinshenk/fer) library based on convolutional neural network is used to detect emotions from facial expression
