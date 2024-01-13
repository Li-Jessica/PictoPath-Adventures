<template>
    <div class="card">
      <v-progress-linear color="rie-primary-color" height="6" rounded :indeterminate="loading"></v-progress-linear>
      <v-card-title bg-color="primary-color" class="card-header">{{ cardData.title }}</v-card-title>
      <div class="card-body">
        <div class="character-dropdown">
          <v-select bg-color="primary-color" @change="changeSelection" v-model="selectedOption" :items="cardData.options" item-title="title" item-value="value" :label="cardData.dopdownLabel" class="mr-4"/>
        </div>
        <img :src="processedImage" alt="" />
        <p>{{ cardData.text }}</p>
        <template v-if="cardData.generateImageFlag">
            <v-btn color="primary-color" @click="generateImage">Generate Image</v-btn>
        </template>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, watch } from 'vue';
  import axios from 'axios';
  
  export default {
    props: {
      cardData: Object
    },
    setup(props) {
      // State
      const loading = ref(false);
      const processedImage = ref('');
      const selectedOption = ref(props.cardData.options[0].value);
  
      // Asynchronous function to process the input and retrieve an image
      const fetchData = async () => {
        // Show loading spinner
        loading.value = true;
  
        try {
          const inputs = {
            prompt: `rainbow ${selectedOption} on a boat in a rain forest in sun hats`
          };
  
          const response = await axios.post('http://127.0.0.1:5000/run_ai', inputs);
  
          // Assuming the Flask backend sends the image data in the response
          const base64Image = response.data.image_data;
          processedImage.value = `data:image/png;base64,${base64Image}`;
  
          console.log("Image generated");
        } catch (error) {
          console.error('Error processing image. Is the back-end running? ', error);
        } finally {
          // Hide loading spinner
          loading.value = false;
        }
      };
  
      // Method to generate image
      const generateImage = () => {
        fetchData();
      };
  
      // Watch for changes in selectedCharacter and trigger fetchData
      watch(selectedOption, () => {
        fetchData();
      });
  
      // Method to handle selection change
      const changeSelection = () => {
        // TBD
      };
  
      return {
        loading,
        processedImage,
        selectedOption,
        characterOptions: props.cardData.options,
        generateImage,
        changeSelection
      };
    }
  };
  </script>
  
  <style scoped>
  .card {
    width: 800px;
    height: 1600px;
    border: 1px solid #ccc;
    margin: 10px;
  }
  
  .card-header {
    background-color: #3498db;
    color: white;
    padding: 10px;
  }
  
  .card-body {
    padding: 20px;
  }
  
  .character-dropdown {
    margin-bottom: 10px;
  }
  
  img {
    max-width: 100%;
    max-height: 100%;
  }
  </style>
  