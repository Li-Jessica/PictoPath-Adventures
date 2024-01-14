<template>
    <div class="card">
      <v-progress-linear color="primary-color" height="6" rounded :indeterminate="loading"></v-progress-linear>
      <v-card-title class="card-header">{{ cardData.title }}</v-card-title>
      <div class="card-body">
        <div v-if="cardData.options.length > 0" class="character-dropdown">
          <v-select bg-color="primary-color" v-model="selectedOption" :items="cardData.options" item-title="title" item-value="title" :label="cardData.dropdownLabel" class="mr-4"/>
        </div>
        <img :src="cardData.image" class="centered-image" alt="" width="300px" />
        <img :src="processedImage" class="centered-image" alt="" width="300px" />
        <p>{{ cardData.text }}</p>
        <p2 v-model="errorMessage"> {{ errorMessage }}</p2>

        <template v-if="cardData.id === 11 || cardData.id === 7">
            <v-text-field label="What treasure do you envision, dear adventurer?" v-model="treasureInput" bg-color="primary-color" class="mr-3"></v-text-field>
        </template>
        
        <template v-if="cardData.generateImageFlag">
            <v-btn color="primary-color" @click="generateImage">Generate Image</v-btn>
        </template>
      </div>
      <v-btn class="ml-auto mr-2 mb-2" color="primary-color" @click="handleNext">Next</v-btn>
    </div>
  </template>
  
  <script>
  import { ref, watch, onMounted } from 'vue';
  import axios from 'axios';
  
  const selectedOption = ref('Make a selection');
  const treasureInput = ref("");
  const errorMessage = ref("");
  
  export default {
    props: {
      cardData: Object,
      adventureState: Object
    },
    methods: {
        handleNext() {
            this.$emit('next');
            selectedOption.value = 'Make a selection';
            errorMessage.value = "";
        }
    },
    setup( props, { emit } ) {
      // State
        const loading = ref(false);
        const processedImage = ref('');
  
        // Asynchronous function to process the input and retrieve an image
        const fetchData = async () => {
            loading.value = true;
            errorMessage.value = "";
    
            try {
                let inputs;
                if( props.cardData.id === 11 || props.cardData.id === 7 ) {
                    inputs = {
                        prompt: `A ${treasureInput.value} treasure chest.`
                    };

                } else {
                    inputs = {
                        prompt: `A ${props.adventureState.character} is havinng a grand ${props.adventureState.adventureType} adventure while carrying ${props.adventureState.item}`
                    };
                }
        
                const response = await axios.post('http://127.0.0.1:5000/run_ai', inputs);
        
                // Assuming the Flask backend sends the image data in the response
                const base64Image = response.data.image_data;

                if( base64Image !== undefined ) {
                    processedImage.value = `data:image/png;base64,${base64Image}`;
                } else {
                    errorMessage.value = "Cloudflare API is currently down.";
                }
            
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
        });

        // Reset selectedOption when the component is mounted
        onMounted(() => {
            selectedOption.value = 'Make a selection';
            if (props.cardData.generateImageFlag) fetchData();
        });
    
        return {
            loading,
            processedImage,
            selectedOption,
            generateImage,
            treasureInput, 
            errorMessage
        };
    }
  };
  </script>
  
  <style scoped>
    .card {
        width: 99%;
        height: 600px;
        border: 1px solid #ccc;
        margin: 10px;
        display: flex;
    }
    
    .card-header {
        background-color: #422c54;
        color: white;
        padding: 10px;
    }
    
    .card-body {
        padding: 20px;
    }
    
    .character-dropdown {
        margin-bottom: 10px;
    }
    
    .centered-image {
        display: block;
        margin: 0 auto;
    }
  </style>
  