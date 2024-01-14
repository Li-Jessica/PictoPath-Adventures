# PictoPath Adventures - SheHacks+ 8 Project

## Inspiration
Our project was sparked by a previous idea we explored earlier this year, revolving around the utilization of Stability AI's Stable Diffusion to generate images for a software architecture project. Although we initially set that concept aside, the introduction of CloudFlare's Workers AI provided a fresh opportunity to revisit and implement it. The intuitive functionality of Workers AI streamlined access to various machine learning models, transforming our initial inspiration into a tangible reality. 

Plus, we wanted to have fun and immerse ourselves into the heart of SheHacks+ 8's theme this year! 

## What it does
Introducing PictoPath (*picture-to-path*), where you craft your unique adventure! Harnessing the power of CloudFlare's Workers AI text-to-image models, users can embark on a personalized journey, choosing between a captivating sea voyage or an enthralling jungle expedition in pursuit of hidden treasure. Immerse yourself in an interactive choose-your-own adventure story, where every decision—from character traits to the paths taken—shapes the unfolding narrative. PictoPath invites users to navigate a world of possibilities and uncover the excitement that lies within their chosen path.

## Project Setup and Pre-requisites 
Prerequisites include Python 3.7+ and npm version 10.2+. The known compatible versions used include Python 3.12 and npm 10.2.4. 

### Required Packages
### Back-end
Please ensure pip3, flask, flask-cors are installed:
```sh
pip install flask
pip install flask-cors
```
### Front-end
Install the front-end project dependencies with the following command:
```sh
npm install
```

### Compile and Hot-Reload for Development
Use the following command when developing locally:
```sh
npm run dev
```

### Compile and Minify for Production
Use the following command to run the optimized, production version:
```sh
npm run build
```

## How we built it
Our team has successfully crafted an interactive story AI application, leveraging a powerful stack of tools to ensure a seamless and dynamic user experience. For the front-end, we used JavaScript while employing Vue.js alongside Vuetify, creating an intuitive and responsive user interface. On the back-end, Python and Flask provided the robust foundation, relaying the user's prompts between the front-end and CloudFlare's text-to-image model.

One of the key highlights of our project is the integration of CloudFlare Workers AI, specifically utilizing Stability AI's Stable Diffusion for text-to-image generation. This cutting-edge technology allows us to bring narratives to life with visually compelling and contextually relevant images, enhancing the overall storytelling experience.

To streamline deployment and ensure efficiency, we've harnessed the capabilities of CloudFlare. We utilized CloudFlare CLI (C3 to create Workers and Wrangler to develop and deploy them) and integrated our Vue project with GitHub. This allowed us to automatically deploy our application every time there's a new commit on the main branch. This not only expedites the deployment process but also ensures that our users access the latest enhancements and features with minimal downtime.

In summary, our full-stack AI application merges the strengths of JavaScript (Vue.js), Python (Flask), and the CloudFlare tech stack (C3, Wrangler, and Workers AI) to deliver an engaging and interactive AI story experience. 

## Challenges we ran into
- unfamiliar with cloudflare and workers ai, needed to figure out how to use workers ai to make requests to use text-to-image
- tokens and keys for cloudflare 
- cloudflare deployment
- cloudflare api model is unreliable, and won't generate images for our prompts as it unavailable sometimes
- godaddy coupon domain didn't work 

## Accomplishments that we're proud of
- built a full-stack application
- auto-deployment
- first time working with a language model/AI
- first time building a back-end
- jessica's first time with vue

## What we learned
- having a plan and vision is important 
- vue and vuetify is a pleasant experience! 
- cloudflare! 
- how to write good prompts for ai models
- axios requests from front-end to back-end 

## What's next for PictoPath-Adventures
- more options to pick from
- more adventures
- optimize user experience with faster image generation

