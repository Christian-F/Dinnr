<template>
  <div id="app">
    <h2>My Food Items</h2>
    <div class="fooditems">
      <FoodItem v-for="(fooditem, index) in foodItems" :key="index" :name="fooditem.name" :brand_name="fooditem.brand_name" />
    </div>
    <h2>Add a new Food Item</h2>
    <form @submit.prevent="addFoodItem">
      Item Name
      <input v-model="newFoodItem.name" placeholder="Food Item">
      Item Brand
      <input v-model="newFoodItem.brand_name" placeholder="Brand Name">
      <button>Add Food Item</button>
    </form>
  </div>
</template>

<script>
import FoodItem from "./components/FoodItem";
import axios from 'axios';

export default {
  name: 'App',
  components: {
    FoodItem,
  },
  data() {
    return {
      foodItems: [],
      newFoodItem: {
        name: "",
        brand_name: "",
      }
    };
  },
  methods: {
    loadFoodItems: function() {
      axios.get('/api/items/').then(
        response => {
          this.foodItems = response.data;
        }
      );
    },
    addFoodItem: function() {
      console.log("Posting new item. Name=" + this.newFoodItem.name + " brand=" + this.newFoodItem.brand_name)
      axios.post('/api/items/', {name: this.newFoodItem.name, brand_name: this.newFoodItem.brand_name}).then(
        response => {
          // Reset the newFoodItem
          this.newFoodItem = "";
          this.foodItems.push(response.data);
        }
      );
    }
  },
  created() {
    this.loadFoodItems();
  },
}
</script>


<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  width: 100vw;
  min-width: 300px;
  max-width: 1000px;
  margin: 0 auto;
}
h2 {
  margin: 10px;
}
form {
  margin: 20px;
  display: flex;
  flex-direction: column;
}
form textarea {
  resize: none;
  height: 220px;
  margin: 0 10px;
  background: beige;
  outline: none !important;
  border: none;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.4);
  border-radius: 5px;
  padding: 10px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 1em;
}
form button {
  background: lightgreen;
  color: darkgreen;
  padding: 10px;
  border: none;
  border-radius: 5px;
  margin: 10px;
  cursor: pointer;
  outline: none !important;
}
form button:hover {
  background-color: #a0fea0;
}
</style>