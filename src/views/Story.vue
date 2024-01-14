<template>
    <div>
      <h1>Welcome to PictoPath Adventures!</h1>      
      <div>
        <StoryItem :cardData="cards[currentCard]" :adventureState="adventureState" @next="goToNextCard" @selectedOption="updateAdventureState"/>
      </div>
    </div>
  </template>
  
  <script>
    import StoryItem from "../components/StoryItem.vue";
    import { ref } from 'vue';
    import cardImage from "../assets/images/banner-2.png";
    
    export default {
        components: {
            StoryItem
        },
    data() {
        return {
            cards: [
                { 
                    title: 'Choose your adventure type', 
                    text: 'Add text',
                    image: cardImage,
                    options: [
                        { title: 'Sea Voyage', value: 'Epic sea voyage adventure'},
                        { title: 'Jungle exploration', value: 'Epic jungle exploration adventure'}],
                    generateImageFlag: false,
                    dropdownLabel: 'Select an adventure theme'
                },
                { 
                    title: 'Choose your character', 
                    text: 'Add text',
                    image: cardImage,
                    options: [
                        { title: 'Bunny', value: 'little bunny' },
                        { title: 'Cat', value: 'little kitty' },
                        { title: 'Dog', value: 'happy puppy' }, ], 
                    generateImageFlag: false,
                    dropdownLabel: 'Select a character'
                },
                { 
                    title: 'Pick an item for your trip', 
                    text: 'Add text', 
                    image: cardImage,
                    options: [
                        { title: 'French fries', value: 'delicious french fries' },
                        { title: 'A lantern', value: 'a glowing lantern' },
                        { title: 'A sun hat', value: 'a yellow straw sun hat' }, ], 
                    generateImageFlag: false,
                    dropdownLabel: 'Select a helpful item for you adventure'
                },
                { 
                    title: 'Say hello to your character!!', 
                    text: 'This is what you look like. Not bad, eh.', 
                    image: "",
                    options: [], 
                    generateImageFlag: true,
                    dropdownLabel: ''
                },
                { 
                    title: 'Ahoy! The start of a grand sea voyage!', 
                    text: 
                    'The sea voyage commenced under the brilliant rays of a warm, sunlit day. \
                    The ship gracefully cut through the calm waters, and a gentle breeze carried the scent of salt and adventure. \
                    You and your companions stood on the deck, basking in the sunlight as the vessel sailed into the horizon. \
                    The atmosphere buzzed with anticipation, and the rhythmic sound of the waves provided a \
                    soothing backdrop to the beginning of your maritime journey. Little did you know that the \
                    tranquility of the day would soon be challenged by the twists of fate on the open sea.', 
                    image: "",
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    title: 'Harmony amidst the great tempest', 
                    text: 
                    'As the storm unleashed its fury, rain lashed against the ship, and the vessel pitched and rolled with the churning waves. \
                    Amidst the chaos, you faced a crucial decision. Would you rally your companions to sing sea shanties, \
                    raising the spirits on board with melodic tunes, or opt for a more relaxed approach by engaging in lively card games to distract from the tempestuous conditions?', 
                    image: "",
                    options: [
                        { title: 'Sing sea shanties', value: 'sing sea shanties' },
                        { title: 'Play some card games', value: 'play card games' }
                    ], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    title: 'Land ho! The Island Expedition', 
                    text: 
                    'Eventually, after enduring the great storm, the clouds began to disperse, and the sun reappeared, \
                    casting a warm glow over the tranquil sea. With relief, you continued your journey and arrived \
                    at a mysterious island. Consulting your weathered treasure map, you and your companions eagerly set out on a new quest, \
                    exploring the uncharted terrain, deciphering clues, and overcoming challenges in pursuit of the hidden treasure.', 
                    image: "",
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    title: 'Seafarer\'s Delight: Riches Beyond the Waves', 
                    text: 
                    'The culmination of your epic voyage was marked by the discovery of the long-lost treasure. \
                    A chest filled with gleaming jewels, ancient artifacts, and secrets untold lay before you. \
                    As you and your companions reveled in the triumph, a question arose – what form would your coveted treasure take? \
                    Would it be a cache of enchanted artifacts, a trove of gold and jewels, or perhaps something entirely unexpected? \
                    The choice is yours, as the spoils of your daring adventure await your decision. What treasure do you envision, dear adventurer?', 
                    image: "",
                    options: [], 
                    generateImageFlag: true,
                    dropdownLabel: ''
                },
                { 
                    title: 'Rainfall Reckoning: The start of jungle adventure!', 
                    text: 
                    'The boat sliced through the murky waters as you and your companions embarked on an epic jungle expedition. \
                    The dense greenery of the rainforest loomed ahead, promising mystery and adventure. However, a few hours into the journey, \
                    the skies darkened, and the sound of thunder rumbled ominously. Suddenly, a torrential downpour soaked everything in its path. \
                    With the rain showing no sign of letting up, you and your companions quickly considered your options. \
                    A debate ensued about seeking shelter under a massive, ancient leaf or finding refuge in a nearby cave. \
                    The decision was crucial, and as the leader of the expedition, you had to choose quickly. \
                    What would it be - the giant leaves or the cave?', 
                    image: "",
                    options: [
                        { title: 'Hide under the leaves', value: 'hide under the big jungle leaves'},
                        { title: 'Hide in the cave', value: 'hide in the jungle cave'}
                    ], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    title: 'Canopy Calm: Stories and Slumber in the Jungle\'s Embrace', 
                    text: 
                    'Now that you have found some shelter, it looks like the rain will be going on for a while.\
                    While waiting for the rain to pass, you and your companions sought solace in various activities.\ Some proposed reading a book to pass the time, while others preferred a quick nap. \
                    The decision was yours to make. What would you suggest to your companions - an immersive book or a rejuvenating nap?',
                    image: "",
                    options: [
                        { title: 'Read a book', value: 'read a book'},
                        { title: 'Take a nap', value: 'take a nap'}
                    ], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    title: 'Trail of Treasures: Navigating the Jungle\'s Hidden Secrets', 
                    text: 
                    'Emerging from the embrace of the storm, you and your companions carried on through the revitalized jungle, \
                    armed with the ancient treasure map. The air was charged with the earthy scent of rain-soaked soil, and the once-muted colors \
                    of the rainforest burst forth in vibrant hues. Sunlight filtered through the canopy, casting enchanting patterns on the damp foliage.\
                    Following the intricate clues on the map, your group weaved through the now-drenched underbrush and crossed crystal-clear streams \
                    formed by the recent downpour. Each step resonated with the renewed spirit of adventure, the post-storm jungle revealing a tapestry of glistening leaves and iridescent insects.\
                    The map, now cradled in your hands, guided your companions with a promise of hidden wonders. The journey became a dance with nature, as the sounds of exotic birds and the distant\
                     murmur of waterfalls accompanied your expedition. How did the jungle\'s transformation after the storm impact your quest, \
                     and what newfound wonders did your companions discover amid the refreshed setting? The unfolding chapters of your adventure \
                     painted a vivid picture of resilience and exploration in the heart of the rejuvenated jungle.',
                    image: "",
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    title: 'The Jewel Unveiled: Triumph and Revelry in Jungle Shadows', 
                    text: 
                    'Following the trail of clues through the dense jungle, your expedition reached a secluded clearing. \
                    The treasure, hidden for centuries, was finally within your grasp. \
                    A lush, vibrant tapestry of flora surrounded the discovery site as you uncovered the long-lost bounty.\
                    The treasure revealed itself to be a trove of natural wonders and ancient artifacts, nestled amidst the roots of an enormous, ancient tree. \
                    The air was thick with a sense of accomplishment as your companions marveled at the eclectic mix of jewels, mysterious relics, and rare flora.\
                    As you and your companions reveled in the triumph of your expedition, you couldn\'t help but wonder: What should the treasure be? It could be a legendary \
                    artifact, a chest filled with jewels, or something entirely unique. What kind of treasure would you like to find at the heart of the ancient temple?', 
                    image: "",
                    options: [], 
                    generateImageFlag: true,
                    dropdownLabel: ''
                },
            ],
            currentCard: 0,
            adventureState: ref({
                adventureType: "voyage",
                character: "bunny",
                item: "a lantern"
            })
        };
    },
    methods: {
        goToNextCard() {
            this.currentCard++;
        },
        updateAdventureState(selectedOption) {
            console.log('Selected Option in Parent:', selectedOption);

            switch (this.currentCard) {
                case 0:
                    this.adventureState.adventureType = selectedOption;
                    break;
                case 1:
                    this.adventureState.character = selectedOption;
                    break;
                case 2:
                    this.adventureState.item = selectedOption;
                    break;
            }
        }
    }
};
</script>
  