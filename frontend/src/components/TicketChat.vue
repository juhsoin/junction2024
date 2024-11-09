<template>
    <v-container>
        
  
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
          <v-btn color="primary" @click="submitNewItem">Add Item</v-btn>
          <v-btn color="secondary" @click="toggleForm">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue';
    

  const props = defineProps<{
  items: Array<{ user: string; description: string }>;
  user: { company: string };
}>();

const emit = defineEmits<{
  (e: 'add-item', item: { user: string; description: string }): void;
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
  
  // Function to submit a new item
  const submitNewItem = () => {
  if (newDescription.value.trim()) {
    const newItem = {
      user: props.user.company,
      description: newDescription.value.trim(),
    };
    emit('add-item', newItem); // Emit the new item to the parent
    newDescription.value = '';
    showForm.value = false;
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
  