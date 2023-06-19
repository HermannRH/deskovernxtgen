<script setup lang="ts">
import { ref, computed } from 'vue';
import { CircleIcon, DotsIcon } from 'vue-tabler-icons';
import { recentEvals } from '@/data/dashboard/dashboardData';
const primaryColors = ['#003f5c', '#58508d', '#bc5090']; // '#003f5c Cuidado', '#58508d EP', '#bc5090 Liderazgo'

// Function to parse date strings in 'dd/mm/yyyy' format to Date objects
const parseDate = (dateStr: string): Date => {
  const [day, month, year] = dateStr.split("/").map(Number);
  return new Date(year, month - 1, day);
};


// Computed property to get the latest 3 changes
const recentEvalsLimited = computed(() => {
  return recentEvals
    .sort((a, b) => parseDate(b.date).getTime() - parseDate(a.date).getTime())
    .slice(0, 8);
});
</script>

<template>
    <v-card elevation="10" class="withbg">
        <v-card-item class="pb-0">
            <v-card-title class="text-h5 pt-sm-2">Evaluaciones Recientes</v-card-title>
            <div class="recent-evals mt-5 px-3">
                <div v-for="list in recentEvalsLimited" :key="list.date">
                    <v-row class="d-flex mb-4">
                        <v-col cols="4" lg="3" md="auto" sm="auto" class="px-0 pt-0 pb-1 d-flex align-start">
                        <div class="fixed">
                            <h6 class="text-body-1 textSecondary text-no-wrap">
                            <span class="text-smaller">{{ list.date }}</span>
                        </h6>
                        </div>
                        </v-col>

                        <v-col cols="1" sm="1" class="px-0 text-center pt-0 pb-1">
                            <div class="circle" :style="{ backgroundColor: list.textcolor }"></div>
                        </v-col>
                        <v-col cols="7" sm="8" class="pt-0 pb-1" >
                            <h6 v-if="list.boldtext" class="text-body-1 font-weight-bold">{{ list.description }}</h6>
                            <h6 v-else class="text-body-1 textSecondary">{{ list.description }}</h6>
                            <div class="mt-n1">
                                <RouterLink :to="list.url" class="text-body-1 text-primary text-decoration-none" v-if="list.link">{{
                                    list.link
                                }}</RouterLink>
                            </div>
                        </v-col>
                    </v-row>
                </div>
            </div>
        </v-card-item>
    </v-card>
</template>
<style lang="scss">
.recent-transaction {
    .line {
        width: 2px;
        height: 35px;
    }
}
.circle {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    display: inline-block;
}
.text-smaller {
    font-size: 12px;
}
.fixed {
  width: 100px; 
  height: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  // Center vertically
  display: flex;
  align-items: center;
}
</style>
