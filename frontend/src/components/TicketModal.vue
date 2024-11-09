<script lang="ts" setup>
import { fetchTicketMeetingNotes, type ITicket } from '@/api/ticket';
import { defineProps, defineEmits, ref } from 'vue';
import { VCard, VCardTitle, VCardText, VBtn, VDivider, VContainer } from 'vuetify/components';
import TicketChat from './TicketChat.vue';
import { EStates } from '@/filters/filter';

// Define the props
const props = defineProps<{
  ticket: ITicket;
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
const publicCommentsVisible = ref(false);
const privateCommentsVisible = ref(false);

const addItemToPublic = (newItem: { user: string; description: string }) => {
  public_save.value.push(newItem);
};
const addItemToPrivate = (newItem: { user: string; description: string }) => {
  private_save.value.push(newItem);
};

const loading = ref(true)

const title = props.ticket.title;
const state = EStates[parseInt(props.ticket.status)]
const category = 'Work'
const description = props.ticket.description;
const release_version = props.ticket.planned_release ?? 'unknown';
const meetingNotes = ref<string[]>([])

fetchTicketMeetingNotes(props.ticket.id ?? '').then((response) => {
  meetingNotes.value = Array.isArray(response) ? response.map(n => n.comment) : [];
  loading.value = false;
})

const user = ref({
  company: 'Fortum 1',
});
const public_save = ref([
    { user: 'Helen 1', description: 'This is the first item.' },
    { user: 'Vattenfal 2', description: 'This is the second item.' },
    { user: 'Fortum 3', description: 'This is the third item.' },
    { user: 'Helen 4', description: 'This is the fourth item.' },
  ]);
  const private_save = ref([
    { user: 'Helen 1', description: 'This is the first item.' },
    { user: 'Vattenfal 2', description: 'This is the second item.' },
    { user: 'Fortum 3', description: 'This is the third item.' },
    { user: 'Helen 4', description: 'This is the fourth item.' },
  ]);

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
              <span class="card-section-title">Description: </span> 
              <p class="text-wrap"> {{ state }} </p>
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
            v-if="meetingNotesVisible && meetingNotes.length"
            v-for="note in meetingNotes"
            class="meeting-note"
          >
          {{ note }}
          <VDivider></VDivider>
          </VCardText>
          <VCardText v-else-if="meetingNotesVisible" class="meeting-note"> Notes not found.</VCardText>

        <VCardText class="card-section-public-comments">
            <span class="card-section-title">Public comments</span>
            <VBtn @click="publicCommentsVisible = !publicCommentsVisible">
              {{ publicCommentsVisible ? 'Hide Comments' : 'Show Comments' }}
            </VBtn>
          </VCardText>
          <VDivider v-if="publicCommentsVisible"></VDivider>
  
        <TicketChat v-if="publicCommentsVisible" :items="public_save" :user="user" @add-item="addItemToPublic" />


        <!-- change the color scheme of the private comment  -->
        <VCardText class="card-section-private-comments">
            <span class="card-section-title">Private comments</span>
            <VBtn @click="privateCommentsVisible = !privateCommentsVisible">
              {{ privateCommentsVisible ? 'Hide Comments' : 'Show Comments' }}
            </VBtn>
          </VCardText>
          <VDivider v-if="privateCommentsVisible"></VDivider>
  
        <TicketChat v-if="privateCommentsVisible" :items="private_save" :user="user" @add-item="addItemToPrivate" />


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
    margin-top: 5px;
    margin-left: 520px;;
    .v-btn {
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