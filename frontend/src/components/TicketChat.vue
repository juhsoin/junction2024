<template>
    <v-container>
        <v-toolbar-title>{{ title }}</v-toolbar-title>
  
      <!-- Displaying the list of items -->
      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index">
          <v-list-item-content>
            <v-list-item-title>{{ item.user }}</v-list-item-title>
            <v-list-item-subtitle>{{ item.description }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
  
      <!-- Button to show the add item form -->
      <v-btn color="primary" @click="toggleForm" v-if="!showForm">Add New Comment</v-btn>
  
      <!-- Form to add a new item, displayed only if showForm is true -->
      <v-card v-if="showForm" class="add-item-form" outlined>
        <v-card-title>Add a New Item</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="newDescription"
            label="Description"
            outlined
            dense
            placeholder="Enter item description"
            auto-grow
            rows="1"
          />
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="addItem">Add Item</v-btn>
          <v-btn color="secondary" @click="toggleForm">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue';
  
  // Sample list of items
  const items = ref([
    { user: 'Item 1', description: 'This is the first item.' },
    { user: 'Item 2', description: 'This is the second item.' },
    { user: 'Item 3', description: 'This is the third item.' },
    { user: 'Item 4', description: 'This is the fourth item.' },
  ]);


  // User who has logged in
  const user = ref({
    company: 'Fortum',
    });
    
    // title props from parent component
    const props = defineProps<{
  title: string;
}>();
  // New item form data
  //const newTitle = ref<string>('');
  const newDescription = ref<string>('');
  
  // Toggle form visibility
  const showForm = ref<boolean>(false);
  
  // Function to toggle the form visibility
  const toggleForm = () => {
    showForm.value = !showForm.value;
    if (!showForm.value) {
      newDescription.value = '';
    }
  };
  
  // Function to add a new item to the list
  const addItem = () => {
    if (newDescription.value.trim()) {
      items.value.push({
        user: user.value.company,
        description: newDescription.value.trim(),
      });
      newDescription.value = '';
      showForm.value = false; // Hide the form after adding the item
    }
  };
  </script>
  
  <style scoped>
.v-list-item-title,
.v-list-item-subtitle {
  white-space: normal;         /* Allows text to wrap to the next line */
  word-break: break-word;      /* Ensures long words break onto a new line */
  overflow-wrap: anywhere;     /* Allows breaking at any character if necessary */
  display: block;              /* Ensures it takes up full width */
}
.v-list-item-content {
  width: 100%;             /* Ensures the content takes full width of the parent */
}
.add-item-form {
  width: 100%;         /* Allow it to take the full width of the parent */

}

  </style>
  