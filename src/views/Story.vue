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
                        { title: 'French fries', value: 'delicius french fries' },
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
  