<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { useTheme } from 'vuetify';
const theme = useTheme();
const primary = theme.current.value.colors.primary;
const lightprimary = theme.current.value.colors.lightprimary;
const max = 10;
const primaryColors = ['#003f5c', '#58508d', '#bc5090']; // '#003f5c Cuidado', '#58508d EP', '#bc5090 Liderazgo'
const missingColors = ['#6699b3', '#9c9bb9', '#f0b9d6'];
const yearlyData = [
    {year: 2022, values: [7, 6, 8]},
    {year: 2023, values: [9, 8, 7]},
];



const currentYearData = computed(() => yearlyData[currentYearIndex.value]); 
const selectedYear = ref(yearlyData[1].year);
const currentYearIndex = ref(yearlyData.findIndex(y => y.year === selectedYear.value));

const chartOptions = computed(() => {
    const yearData = currentYearData.value;
    const labels = ['Cuidado PI', 'Espacios Públicos PI', 'Liderazgo PI'];
    const missingLabels = ['Cuidado PI Restante', 'Espacios Públicos PI Restante', 'Liderazgo PI Restante'];

    const series = yearData.values.map(val => (val / max) * 100);
    const missingSeries = yearData.values.map(val => ((max - val) / max) * 100);
    let mergedLabels = [];
    let mergedSeries = [];
    let mergedColors = [];
    for(let i = 0; i < labels.length; i++) {
        mergedLabels.push(labels[i], missingLabels[i]);
        mergedSeries.push(series[i], missingSeries[i]);
        mergedColors.push(primaryColors[i], missingColors[i]);
    }
    return {
    labels: mergedLabels,
    series: mergedSeries,
    chart: {
        type: 'donut',
        fontFamily: `inherit`,
        foreColor: '#a1aab2',
        toolbar: { show: false }
    },
    colors: mergedColors,
    plotOptions: {
        pie: {
            startAngle: 0,
            endAngle: 360,
            donut: { size: '75%', background: 'transparent' }
        }
    },
    stroke: { show: false },
    dataLabels: { enabled: false },
    legend: { show: false },
    tooltip: { 
        theme: "light",
        followCursor: false,
    },
};
});


const average = computed(() => {
    const yearData = currentYearData.value;
    return (yearData.values.reduce((a, b) => a + b, 0) / yearData.values.length).toFixed(1);
});

const percentChange = computed(() => {
    if (currentYearIndex.value === 0) return 0;
    const lastYearAvg = (yearlyData[currentYearIndex.value - 1].values.reduce((a, b) => a + b, 0) / yearlyData[currentYearIndex.value - 1].values.length);
    const currentYearAvg = (yearlyData[currentYearIndex.value].values.reduce((a, b) => a + b, 0) / yearlyData[currentYearIndex.value].values.length);
    return ((currentYearAvg - lastYearAvg) / lastYearAvg * 100).toFixed(1);
});

watch(selectedYear, (newYear) => {
  currentYearIndex.value = yearlyData.findIndex(y => y.year === newYear);
});

const selectYear = (year: number) => {
  selectedYear.value = year;
};
</script>

<template>
    <v-card elevation="10" class="withbg" >
        <v-card-item id="hi2">
            <div class="d-sm-flex align-center justify-space-between pt-sm-2">
                <v-card-title class="text-h5">Portafolio de Inversiones</v-card-title>
            </div>
            <v-row id="hi3">
                <v-col cols="7" sm="7">
                    <div>
                    <span v-for="(data, index) in yearlyData" :key="index"
                          :class="{ 'font-weight-bold': selectedYear === data.year }"
                          @click="selectYear(data.year)" class="text-secondary mr-2 selectable-year">
                        {{ data.year }}
                    </span>
                </div>
                    <div class="mt-6">
                        <h3 class="text-h3">{{ average }}</h3>
                        <div class="mt-1">
                            <v-avatar class="bg-lightsuccess text-success" size="25">
                                <ArrowUpLeftIcon size="20" />
                            </v-avatar>
                            <span class="text-subtitle-1 ml-2 font-weight-bold">{{ percentChange }}%</span>
                            <span class="text-subtitle-1 text-muted ml-2">último año</span>
                        </div>
                    </div>
                </v-col>
                <v-col cols="5" sm="5" class="pl-lg-0">
                    <div  class="d-flex align-center flex-shrink-0">
                        <apexchart class="pt-6" type="donut" height="145" :options="chartOptions" :series="chartOptions.series" :key="selectedYear"></apexchart>
                    </div>
                </v-col>
            </v-row>
        </v-card-item>
    </v-card>
</template>
<style scoped>
.selectable-year {
    cursor: pointer;
}
.allow-overflow {
  overflow: visible !important;
  display: initial;
}
</style>

