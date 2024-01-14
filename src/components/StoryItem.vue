<template>
    <div class="card">
      <v-progress-linear color="primary-color" height="6" rounded :indeterminate="loading"></v-progress-linear>
      <v-card-title class="card-header">{{ cardData.title }}</v-card-title>
      <div class="card-body">
        <div v-if="cardData.options.length > 0" class="character-dropdown">
          <v-select bg-color="primary-color" v-model="selectedOption" :items="cardData.options" item-title="title" item-value="title" :label="cardData.dropdownLabel" class="mr-4"/>
        </div>
        <img :src="cardData.image" alt="" width="300px" />
        <img :src="processedImage" alt="" width="300px" />
        <p>{{ cardData.text }}</p>
        <template v-if="cardData.generateImageFlag">
            <v-btn color="primary-color" @click="generateImage">Generate Image</v-btn>
        </template>
      </div>
      <v-btn class="ml-auto" color="primary-color" @click="this.$emit('next')">Next</v-btn>
    </div>
  </template>
  
  <script>
  import { ref, watch, toRefs } from 'vue';
  import axios from 'axios';
  
  export default {
    props: {
      cardData: Object,
      adventureState: Object
    },
    setup(props, { emit } ) {
      // State
      const loading = ref(false);
      const processedImage = ref('');
      const selectedOption = ref(props.cardData.options[0].title);
      const { adventureState } = toRefs(props);
  
      // Asynchronous function to process the input and retrieve an image
      const fetchData = async () => {
        loading.value = true;
  
        try {
          const inputs = {
            prompt: `A ${adventureState.character} is havinng a grand ${adventureState.adventureType} adventure while carrying ${adventureState.item}`
          };
  
          const response = await axios.post('http://127.0.0.1:5000/run_ai', inputs);
  
          // Assuming the Flask backend sends the image data in the response
          const base64Image = response.data.image_data;
          processedImage.value = `data:image/png;base64,${base64Image}`;
  
          console.log("Image generated");
        } catch (error) {
          console.error('Error processing image. Is the back-end running? ', error);
        } finally {
          loading.value = false;
        }
      };
  
      // Method to generate image
      const generateImage = () => {
        fetchData();
      };
  
      // Watch for changes in selectedCharacter and trigger fetchData
      watch(selectedOption, (newValue) => {
        emit('selectedOption', newValue);
        if (props.cardData.generateImageFlag) fetchData();
      });
  
      return {
        loading,
        processedImage,
        selectedOption,
        generateImage
      };
    }
  };
  </script>
  
  <style scoped>
  .card {
    width: 100%;
    height: 600px;
    border: 1px solid #ccc;
    margin: 10px;
  }
  
  .card-header {
    background-color: #f8bdc4;
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
  