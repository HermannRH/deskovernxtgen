<script setup lang="ts">
/*Call Components*/
import Overview from '@/components/dashboard/Overview.vue';
import AveragePerformance from '@/components/dashboard/AveragePerformance.vue';
import VidasImpactadas from '@/components/dashboard/VidasImpactadas.vue';
import RecentEvals from '@/components/dashboard/RecentEvals.vue';
import ActiveInvestments from '@/components/dashboard/ActiveInvestments.vue';
</script>
<template>
    <v-row id>
        <v-col cols="12" >
            <v-row>
                <!-- Visión general -->
                <v-col cols="12" lg="8" class="d-flex" style="min-height: 100%;">
                    <Overview />
                </v-col>
                <!-- AveragePerformance and VidasImpactadas -->
                <v-col cols="12" lg="4" class="d-flex flex-column">
                    <div class="flex-grow-1 d-flex">
                        <AveragePerformance />
                    </div>
                    <div class="flex-grow-1 d-flex">
                        <VidasImpactadas />
                    </div>
                </v-col>
                <!-- Recent transaction -->
                <v-col cols="12" lg="4" class="d-flex" style="min-height: 100%;">
                    <RecentEvals />
                </v-col>
                <!-- Product performance -->
                <v-col cols="12" lg="8" class="d-flex notoverflow" style="min-height: 100%;">
                    <ActiveInvestments />
                </v-col>
            </v-row>
        </v-col>
        <v-col class="text-center mt-2">
            <p class="text-muted">Fundación FEMSA</p>
        </v-col>
    </v-row>
</template>



<style>
.v-card-item__content {
  overflow: visible !important;
  display: initial;
}
.notoverflow {
  overflow: hidden !important;
}
</style>


