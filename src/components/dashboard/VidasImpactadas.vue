<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { MoodOffIcon } from 'vue-tabler-icons';
import { useTheme } from 'vuetify';
const theme = useTheme();
const primary = theme.current.value.colors.primary;
const secondary = theme.current.value.colors.secondary;

const yearlyData = [
    {
        year: 2023,
        labels: ["CJ", "Fondo DIT", "AIPI", "Equimundo", "LAJ", "ExM", "CPI"],
        values: [1500, 200, 340, 900, 789, 200, 20]
    },
    {
        year: 2022,
        labels: ["Fondo DIT", "CPI","EX1","EX2"],
        values: [200,9000,900,1800]
    },
];
yearlyData.sort((a, b) => a.year - b.year);

const selectedYear = ref(yearlyData[1].year);
const currentYearData = computed(() => yearlyData.find(y => y.year === selectedYear.value));
const previousYearData = computed(() => yearlyData.find(y => y.year === selectedYear.value - 1));

const areachartOptions = computed(() => {
    return {
        labels: currentYearData.value ? currentYearData.value.labels : [],
        chart: {
            type: 'area',
            height: 60,
            fontFamily: `inherit`,
            foreColor: '#a1aab2',
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: true
            },
            group: 'sparklines'
        },
        colors: [secondary],
        stroke: {
            curve: 'smooth',
            width: 2
        },
        fill: {
            type: 'solid',
            opacity: 0.05
        },
        markers: {
            size: 0
        },
        tooltip: {
            theme: 'light',
            x: {
                show: true
            }
        },
        annotations: {
            yaxis: [{
                y: goal,
                borderColor: '#FFD700',
                label: {
                    borderColor: '#FFD700',
                    style: {
                        color: '#fff',
                        background: '#FFD700',
                    },
                }
            }],
        },
    };
});
const getCumulativeValues = (values: number[]) => {
    let result = [];
    let runningTotal = 0;
    for (let i = 0; i < values.length; i++) {
        runningTotal += values[i];
        result.push(runningTotal);
    }
    return result;
};

const areaChart = computed(() => {
    return {
        series: [
            {
                name: '',
                data: currentYearData.value ? getCumulativeValues(currentYearData.value.values) : []
            }
        ]
    };

});


const totalImpactedLives = computed(() => {
  const data = currentYearData.value;
  if (!data) return 0;
  return data.values.reduce((a: number, b: number) => a + b, 0);
});

const percentChange = computed(() => {
    if (!previousYearData.value) return 0;
    const lastYearTotal = previousYearData.value.values.reduce((a, b) => a + b, 0);
    return ((totalImpactedLives.value - lastYearTotal) / lastYearTotal * 100).toFixed(1);
});

const selectYear = (year: number) => {
  selectedYear.value = year;
};
const goal = 10000;
const isGoalMet = computed(() => totalImpactedLives.value >= goal);
const goalClass = computed(() => isGoalMet.value ? 'text-success' : 'text-warning');
</script>
<template>
    <v-card elevation="10" class="withbg">
        <v-card-item>
            <div class="d-flex align-center justify-space-between pt-sm-2">
                <v-card-title class="text-h5">Vidas Impactadas</v-card-title>
            </div>
            <v-row>
                <v-col cols="12">
                <div class="d-flex justify-space-between">
                    <div>                    
                        <span v-for="(data, index) in yearlyData" :key="index"
                            :class="{ 'font-weight-bold': selectedYear === data.year }"
                            @click="selectYear(data.year)" class="text-secondary mr-2 selectable-year">
                            {{ data.year }}
                        </span>
                    </div>
                    <v-btn id="item4" size="25" icon  :class="{'bg-success ': isGoalMet, 'bg-warning': !isGoalMet}">
                        <v-avatar size="medium">
                            <MoodOffIcon v-if="!isGoalMet" size="15" class="icon-white" />
                            <TrophyIcon v-else size="15" class="icon-white" />
                        </v-avatar>
                    </v-btn>
                </div>
                    <div class="d-flex justify-space-between align-center">
                        <div>
                            <h3 class="text-h3">{{ totalImpactedLives.toLocaleString() }}</h3>
                            <div class="mt-1">
                                <v-avatar class="bg-lighterror text-accent" size="25">
                                    <ArrowDownRightIcon size="20" />
                                </v-avatar>
                                <span class="text-subtitle-1 ml-2 font-weight-bold">{{ percentChange }}%</span>
                                <span class="text-subtitle-1 text-muted ml-2">último año</span>
                            </div>
                        </div>
                        <div class="d-flex align-center">
                        <h4 :class="goalClass">Meta: {{ goal.toLocaleString() }}</h4>
                    </div>
                </div>
                </v-col>
            </v-row>
        </v-card-item>
        <div >
            <apexchart type="area" height="60" :options="areachartOptions" :series="areaChart.series"> </apexchart>
        </div>
    </v-card>
</template>
<style scoped>
.icon-white svg {
    fill: white;
    stroke: white;
}
</style>
