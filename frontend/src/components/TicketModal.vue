<script lang="ts" setup>
import { defineProps, defineEmits, ref } from 'vue';
import { VCard, VCardTitle, VCardText, VCardActions, VBtn, VDialog, VDivider, VContainer } from 'vuetify/components';

// Define the props
const props = defineProps<{
}>();

// Emit an action event when the button is clicked
const emit = defineEmits<{
  (e: 'action-clicked'): void;
}>();

// Handle action button click
const handleActionClick = () => {
  emit('action-clicked');
};

const meetingNotesVisible = ref(false);

const title = "First ticket"
const state = 'In progress'
const category = 'wörk'
const description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus' +
  	'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
const meetingNotes = ['good', 'poopoo', 'nice']
const publicComments = ['comment', 'comment', 'comment']
const privateComments = ['comment', 'comment', 'comment']
const release_version = '3.2.1'
</script>

<template>
  <VContainer>
   <VCard class="ticket-card">
        <div class="modal-header-section">
          <div class="modal-header-details">
            <VCardTitle>
              {{ title }}
            </VCardTitle>
            <VCardText>
              <span class="card-section-title">State: </span> {{ state }}
            </VCardText>
            <VCardText>
              <span class="card-section-title">Category: </span>{{ category }}
            </VCardText>
            <VCardText>
              <span class="card-section-title">Planned release: </span>{{ release_version }}
            </VCardText>
          </div>
          <div class="modal-header-interactions">
            <VBtn icon="mdi-thumb-up" color="primary"></VBtn> <br>
            <VBtn color="primary">Follow</VBtn>
          </div>
        </div>
        <VDivider></VDivider>
        <VCardText class="card-section-top">
          <span class="card-section-title">Description: </span> {{ description }} <br/>
          <VBtn
           :onclick="() => meetingNotesVisible = !meetingNotesVisible"
           class="modal-card-button"
           >
           Show meeting notes</VBtn>
        </VCardText>
        <VDivider></VDivider>
          <VCardText
            v-if="meetingNotesVisible"
            v-for="note in meetingNotes"
            class="meeting-note"
          >
          {{ note }}
          <VDivider></VDivider>
        </VCardText>

        <VCardText class="card-section-public-comments">
          <span class="card-section-title">Public comments</span>
          <VBtn>Add comment</VBtn>
        </VCardText>
        <VDivider></VDivider>
          <VCardText
            v-for="comment in publicComments"
            class="meeting-note"
          >
          {{ comment }}
          <VDivider></VDivider>
        </VCardText>

        <VCardText class="card-section-private-comments">
          <span class="card-section-title">Private comments</span>
          <VBtn>Add comment</VBtn>
        </VCardText>
        <VDivider></VDivider>
          <VCardText
            v-for="comment in privateComments"
            class="meeting-note"
          >
          {{ comment }}
          <VDivider></VDivider>
        </VCardText>
  </VCard>
  </VContainer>
</template>

<style scoped>

.modal-card {
  width: 1000px;
  max-width: 1000px !important;
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}


.v-card-title {
  color: var(--brand-primary-red);
}

.modal-header-section {
  display: grid;

  .modal-header-details {
    grid-column: 1;
  }

  .modal-header-interactions {
    grid-column: 2;
    margin-top: 40px;
    .v-btn {
      align-self: end;
      margin-top: 15px;
    }
  }
}

.card-section-title {
  font-weight: bold;
}

.card-section-top {
  background-color: var(--brand-lighter-blue-gray);
}

.card-section-public-comments {
  background-color: var(--brand-green);
  .v-btn {
    color: var(--brand-light-blue-gray);
    margin-left: 20px;
  }
}

.card-section-private-comments {
  background-color: var(--brand-green);
  .v-btn {
    color: var(--brand-light-blue-gray);
    margin-left: 20px;;
  }
}

.modal-card-button {
  margin-top: 10px;
  color: var(--brand-light-blue-gray)
}

.meeting-note {
  background-color: var(--brand-lightest-blue-gray);
}

</style>