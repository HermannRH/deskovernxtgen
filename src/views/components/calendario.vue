<template>
    <v-container>
      <v-row>
        <v-col cols="8">
          <iframe 
            src="https://calendar.google.com/calendar/embed?src=en.usa%23holiday%40group.v.calendar.google.com"
            style="border: 0" 
            width="100%" 
            height="600" 
            frameborder="0" 
            scrolling="no">
          </iframe>
        </v-col>
        <v-col cols="2">
          <v-card>
            <v-card-title>Next Event</v-card-title>
            <v-card-text>{{ nextEvent.summary }} at {{ nextEvent.start.dateTime }}</v-card-text>
          </v-card>
        </v-col>
        <v-col cols="2">
          <v-list>
            <v-list-item-group>
              <v-list-item v-for="meta in metas" :key="meta.id">
                <v-list-item-content>{{ meta.title }}</v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        nextEvent: {
          summary: "Next Meeting",
          start: {
            dateTime: "2023-06-20T15:30:00"
          }

        },
        metas: [
          { id: 1, title: "Meta 1" },
          { id: 2, title: "Meta 2" },
          { id: 3, title: "Meta 3" },
        ]
      }
    },
  }
  </script>
  
  