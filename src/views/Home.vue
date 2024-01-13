<template>
    <div>
      <h1>Welcome to PictoPath Adventures!</h1>      
      <div>
        <StoryItem :cardData="cards[currentCard]" :dropdownOptions="page1options "/>
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
        { title: 'Card 1', text: 'Some text for Card 1', imageUrl: 'path/to/image1.jpg' },
        { title: 'Card 2', text: 'Some text for Card 2', imageUrl: 'path/to/image2.jpg' },
        // Add more cards as needed
      ],
      currentCard: 0,
      page1options: [
        { title: 'Bunny', value: 'little bunny' },
        { title: 'Cat', value: 'lithe kitty' },
        { title: 'Dog', value: 'happy puppy' },
        { title: 'None', value: null }
      ]
    };
  },
  methods: {
    goToNextCard() {
      // Logic to move to the next card
      this.currentCard++;

      // Optionally, you can reset to the first card when you reach the end
      if (this.currentCard >= this.cards.length) {
        this.currentCard = 0;
      }
    }
  }
};
</script>
  