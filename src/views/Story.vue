<template>
    <div>
      <h1>Welcome to PictoPath Adventures!</h1>
      {{ errorMessage }}     
      <div>
        <StoryItem :cardData="cards[currentCard]" :adventureState="adventureState" @next="goToNextCard" @selectedOption="updateAdventureState"/>
      </div>
    </div>
  </template>
  
  <script>
    import StoryItem from "../components/StoryItem.vue";
    import { ref } from 'vue';

    import cardImage from "../assets/images/banner-2.png";
    import adventurerBunny from "../assets/images/adventurer-bunny.jpeg";
    import junggleLeaves from "../assets/images/jungle-leaves.jpeg";
    import book from "../assets/images/book.jpeg";
    import lantern from "../assets/images/lantern.jpg";
    import seaVoyage from "../assets/images/sea-voyage.jpg";
    import seaVoyageStorm from "../assets/images/sea-voyage-storm.jpg";
    import shore from "../assets/images/shore.jpg";
    import jungle from "../assets/images/jungle.jpg";

    export default {
        components: {
            StoryItem
        },
    data() {
        return {
            cards: [
                {
                    id: 0,
                    title: 'Choose your adventure type', 
                    text: 'Welcome to PictoPath Adventures!\
                    Embark on an exhilarating journey with our interactive story AI application, where you have the power to shape your destiny. \
                    Choose between two captivating stories that promise adventure beyond your wildest dreams. \
                    Dive into the vast unknown with an epic sea voyage, where the boundless horizon beckons, and the salty breeze whispers secrets \
                    of undiscovered lands. Alternatively, immerse yourself in the heart of the untamed wilderness with a jungle exploration adventure, \
                    where every step unveils the mysteries of ancient ruins and hidden treasures. \
                    The choice is yours, and the adventure begins with a single click. Are you ready to chart your course and experience the thrill of a lifetime?',
                    image: cardImage,
                    options: [
                        { title: 'Sea Voyage', value: 'Epic sea voyage adventure'},
                        { title: 'Jungle exploration', value: 'Epic jungle exploration adventure'}],
                    generateImageFlag: false,
                    dropdownLabel: 'Select an adventure theme'
                },
                { 
                    id: 1,
                    title: 'Choose your character', 
                    text: 'Congratulations on selecting your chosen adventure! Now, it\'s time to add a personal touch to your journey. \
                    Before you set sail on your epic sea voyage or delve into the heart of the jungle, pick a character to accompany\
                     you on this unforgettable quest. Will you be guided by the agility and curiosity of a bunny, the loyal and \
                     adventurous spirit of a dog, or the mysterious and independent nature of a cat? The fate of your expedition lies \
                     not only in the choices you make but also in the companionship you keep. Select your character wisely, and let the adventure with your newfound companion begin!',
                    image: adventurerBunny,
                    options: [
                        { title: 'Bunny', value: 'little bunny' },
                        { title: 'Cat', value: 'little kitty' },
                        { title: 'Dog', value: 'happy puppy' }, ], 
                    generateImageFlag: false,
                    dropdownLabel: 'Select a character'
                },
                { 
                    id: 2,
                    title: 'Pick an item for your trip', 
                    text: 
                    'With your chosen character by your side, it\'s time to pack a crucial item for your upcoming adventure. \
                    Will you bring the comfort of familiar and tasty French fries, adding a delightful snack to your journey? \
                    Alternatively, you might opt for a lantern, illuminating the path ahead and revealing hidden mysteries in the shadows. \
                    Or, perhaps, shield yourself from the elements with a stylish sun hat, providing both protection and a touch of flair. \
                    The choice is yours – select your item wisely, and let the essence of your chosen possession enhance the unfolding tale of your epic sea voyage or jungle exploration. The adventure awaits!', 
                    image: lantern,
                    options: [
                        { title: 'French fries', value: 'delicious french fries' },
                        { title: 'A lantern', value: 'a glowing lantern' },
                        { title: 'A sun hat', value: 'a yellow straw sun hat' }, ], 
                    generateImageFlag: false,
                    dropdownLabel: 'Select a helpful item for you adventure'
                },
                { 
                    id: 3,
                    title: 'Say hello to your character!!', 
                    text: 'This is what you look like. Not bad, eh ;)', 
                    image: "",
                    options: [], 
                    generateImageFlag: true,
                    dropdownLabel: ''
                },
                { 
                    id: 4,
                    title: 'Ahoy! The start of a grand sea voyage!', //4
                    text: 
                    'The sea voyage commenced under the brilliant rays of a warm, sunlit day. \
                    The ship gracefully cut through the calm waters, and a gentle breeze carried the scent of salt and adventure. \
                    You and your companions stood on the deck, basking in the sunlight as the vessel sailed into the horizon. \
                    The atmosphere buzzed with anticipation, and the rhythmic sound of the waves provided a \
                    soothing backdrop to the beginning of your maritime journey. Little did you know that the \
                    tranquility of the day would soon be challenged by the twists of fate on the open sea.', 
                    image: seaVoyage,
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    id: 5,
                    title: 'Harmony amidst the great tempest', 
                    text: 
                    'As the storm unleashed its fury, rain lashed against the ship, and the vessel pitched and rolled with the churning waves. \
                    Amidst the chaos, you faced a crucial decision. Would you rally your companions to sing sea shanties, \
                    raising the spirits on board with melodic tunes, or opt for a more relaxed approach by engaging in lively card games to distract from the tempestuous conditions?', 
                    image: seaVoyageStorm,
                    options: [
                        { title: 'Sing sea shanties', value: 'sing sea shanties' },
                        { title: 'Play some card games', value: 'play card games' }
                    ], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    id: 6,
                    title: 'Land ho! The Island Expedition', 
                    text: 
                    'Eventually, after enduring the great storm, the clouds began to disperse, and the sun reappeared, \
                    casting a warm glow over the tranquil sea. With relief, you continued your journey and arrived \
                    at a mysterious island. Consulting your weathered treasure map, you and your companions eagerly set out on a new quest, \
                    exploring the uncharted terrain, deciphering clues, and overcoming challenges in pursuit of the hidden treasure.', 
                    image: shore,
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    id: 7,
                    title: 'Seafarer\'s Delight: Riches Beyond the Waves', // 7
                    text: 
                    'The culmination of your epic voyage was marked by the discovery of the long-lost treasure. \
                    A chest filled with gleaming jewels, ancient artifacts, and secrets untold lay before you. \
                    As you and your companions reveled in the triumph, a question arose – what form would your coveted treasure take? \
                    Would it be a cache of enchanted artifacts, a trove of gold and jewels, or perhaps something entirely unexpected? \
                    The choice is yours, as the spoils of your daring adventure await your decision.', 
                    image: "",
                    options: [], 
                    generateImageFlag: true,
                    dropdownLabel: ''
                },
                { 
                    id: 8,
                    title: 'Rainfall Reckoning: The start of jungle adventure!', //8
                    text: 
                    'The boat sliced through the murky waters as you and your companions embarked on an epic jungle expedition. \
                    The dense greenery of the rainforest loomed ahead, promising mystery and adventure. However, a few hours into the journey, \
                    the skies darkened, and the sound of thunder rumbled ominously. Suddenly, a torrential downpour soaked everything in its path. \
                    With the rain showing no sign of letting up, you and your companions quickly considered your options. \
                    A debate ensued about seeking shelter under a massive, ancient leaf or finding refuge in a nearby cave. \
                    The decision was crucial, and as the leader of the expedition, you had to choose quickly. \
                    What would it be - the giant leaves or the cave?', 
                    image: junggleLeaves,
                    options: [
                        { title: 'Hide under the leaves', value: 'hide under the big jungle leaves'},
                        { title: 'Hide in the cave', value: 'hide in the jungle cave'}
                    ], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    id: 9,
                    title: 'Canopy Calm: Stories and Slumber in the Jungle\'s Embrace', 
                    text: 
                    'Now that you have found some shelter, it looks like the rain will be going on for a while.\
                    While waiting for the rain to pass, you and your companions sought solace in various activities.\ Some proposed reading a book to pass the time, while others preferred a quick nap. \
                    The decision was yours to make. What would you suggest to your companions - an immersive book or a rejuvenating nap?',
                    image: book,
                    options: [
                        { title: 'Read a book', value: 'read a book'},
                        { title: 'Take a nap', value: 'take a nap'}
                    ], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    id: 10,
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
                    image: jungle,
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
                { 
                    id: 11,
                    title: 'The Jewel Unveiled: Triumph and Revelry in Jungle Shadows', //11
                    text: 
                    'Following the trail of clues through the dense jungle, your expedition reached a secluded clearing. \
                    The treasure, hidden for centuries, was finally within your grasp. \
                    A lush, vibrant tapestry of flora surrounded the discovery site as you uncovered the long-lost bounty.\
                    The treasure revealed itself to be a trove of natural wonders and ancient artifacts, nestled amidst the roots of an enormous, ancient tree. \
                    The air was thick with a sense of accomplishment as your companions marveled at the eclectic mix of jewels, mysterious relics, and rare flora.\
                    As you and your companions reveled in the triumph of your expedition, you couldn\'t help but wonder: What should the treasure be? It could be a legendary \
                    artifact, a chest filled with jewels, or something entirely unique.', 
                    image: "",
                    options: [], 
                    generateImageFlag: true,
                    dropdownLabel: ''
                },
                { 
                    id: 12,
                    title: 'The End!', //12
                    text: 
                    'This is the end of your adventure. Rest easy and until next time dear adventurer!', 
                    image: "",
                    options: [], 
                    generateImageFlag: false,
                    dropdownLabel: ''
                },
            ],
            currentCard: 0,
            adventureState: ref({
                adventureType: null,
                character: null,
                item: null
            }),
            errorMessage: ref(''),
        };
    },
    methods: {
        goToNextCard() {
            this.errorMessage = "";
            if( (this.currentCard === 0 && this.adventureState.adventureType === null) || 
            (this.currentCard === 1 && (this.adventureState.character === null || this.adventureState.character === "Make a selection")) ||
            (this.currentCard === 2 && (this.adventureState.item === null || this.adventureState.item === "Make a selection")) ) {
                this.errorMessage = "Please make a selection to proceed.";
                return;
            }

            if( this.currentCard === 3 ) {
                if( this.adventureState.adventureType === "Sea Voyage" ) {
                    this.currentCard = 4;
                } else {
                    this.currentCard = 8;
                }
            } else if( this.currentCard === 11 || this.currentCard === 7 ) {
                this.currentCard = 12;
            } else if( this.currentCard !== 12 ) {
                this.currentCard++;
            }

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
  