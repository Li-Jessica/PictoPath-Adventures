<template>
    <div>
      <h1>Welcome to PictoPath Adventures!</h1>      
      <div>
        <StoryItem :cardData="cards[currentCard]"/>
      </div>
    </div>
  </template>
  
  <script>
    import StoryItem from "../components/StoryItem.vue";
    
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
                    options: [
                        { title: 'Sea Voyage', value: 'Epic sea yoyage adventure'},
                        { title: 'Jungle exploration', value: 'Epic jungle exploration adventure'}],
                    generateImageFlag: false,
                    dopdownLabel: 'Select an adventure theme'
                },
                { 
                    title: 'Choose your character', 
                    text: 'Add text', 
                    options: [
                        { title: 'Bunny', value: 'little bunny' },
                        { title: 'Cat', value: 'lithe kitty' },
                        { title: 'Dog', value: 'happy puppy' }, ], 
                    generateImageFlag: false,
                    dopdownLabel: 'Select a character'
                },
                { 
                    title: 'Pick an item for your trip', 
                    text: 'Add text', 
                    options: [
                        { title: 'French fries', value: 'delicius french fries' },
                        { title: 'A lantern', value: 'a glowing lantern' },
                        { title: 'A sun hat', value: 'a yellow straw sun hat' }, ], 
                    generateImageFlag: false,
                    dopdownLabel: 'Select a helpful item for you adventure'
                },
            ],
            currentCard: 0
        };
    },
    methods: {
        goToNextCard() {
        // Logic to move to the next card
        this.currentCard++;
        }
    }
};
</script>
  