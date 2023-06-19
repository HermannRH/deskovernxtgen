<script setup lang="ts">
import { ref, watch } from 'vue';
import { computed } from 'vue';
import { useTheme } from 'vuetify';
const theme = useTheme();
const primary = theme.current.value.colors.primary;
const secondary = theme.current.value.colors.secondary;
const select = ref('Distrito 3');
const items = ref(['Distrito 3', 'Edomex', 'Región Sur']);

const chartData = computed(() => {
  switch(select.value) {
    case 'Distrito 3':
      return [10, 9.5, 8.0, 9, 9.9, 8.9, 6, 10];
    case 'Edomex':
      return [9, 8.5, 8.3, 8.8, 7.9, 8.2, 7, 9];
    case 'Liderazgo PI':
      return [9.5, 8, 7.8, 8.5, 9.3, 8.4, 6.5, 9.5];
    default:
      return [10, 9.5, 8.0, 9, 9.9, 8.9, 6, 10];
  }
});

const chartCategories = computed(() => {
  switch(select.value) {
    case 'Distrito 3':
      return ["Sección1", "Sección2", "Sección3", "Sección4", "Sección5", "Sección6", "Sección7", "Sección8"];
    case 'EdomexI':
      return ["Sección9", "Sección10", "Sección11", "Sección12", "Sección13", "Sección14", "Sección15", "Sección16"];
    case 'Región Sur':
      return ["Sección17", "Sección18", "Sección19", "Sección20", "Sección21", "Sección22", "Sección23", "Sección24"];
    default:
      return ["Sección1", "Sección2", "Sección3", "Sección4", "Sección5", "Sección6", "Sección7", "Sección8"];
  }
});

const chartColor = computed(() => {
    switch(select.value) {
        case 'Cuidado PI':
            return '#003f5c';
        case 'Edomex':
            return '#58508d';
        case 'Liderazgo PI':
            return '#bc5090';
        default:
            return '#003f5c';
    }
});
const chartOptions = computed(() => {
    return {
        series: [
            { name: "Calificación General:", data: chartData.value },
        ],
        chartOptions: {
            grid: {
                borderColor: 'rgba(0,0,0,0.1)',
                strokeDashArray: 3,
                xaxis: {
                    lines: {
                        show: false
                    }
                },
            },
            plotOptions: {
                bar: { horizontal: false, columnWidth: "35%", borderRadius: [8] },
            },
            colors: [chartColor.value],
            chart: {
                type: "bar",
                height: 370,
                offsetX: -15,
                toolbar: { show: true },
                foreColor: "#adb0bb",
                fontFamily: 'inherit',
                sparkline: { enabled: false },
            },
            dataLabels: { enabled: false },
            markers: { size: 0 },
            legend: { show: false },
            xaxis: {
                type: "category",
                categories: chartCategories.value,
                labels: {
                    style: { cssClass: "grey--text lighten-2--text fill-color" },
                },
            },
            yaxis: {
                show: true,
                min: 0,
                max: 10,
                tickAmount: 4,
                labels: {
                    style: {
                        cssClass: "grey--text lighten-2--text fill-color",
                    },
                },
            },
            stroke: {
                show: true,
                width: 3,
                lineCap: "butt",
                colors: ["transparent"],
            },
            tooltip: { theme: "light" },

            responsive: [
            {
                breakpoint: 600,
                options: {
                    plotOptions: {
                        bar: {
                            borderRadius: 3,
                        }
                    },
                }
            }
        ]

        },
    };
});
watch(select, () => {
  chartOptions.value.series[0].data = chartData.value;
  chartOptions.value.chartOptions.xaxis.categories = chartCategories.value;
});
</script>
<template>
    <v-card elevation="10" class="withbg">
        <v-card-item>
            <div class="d-sm-flex align-center justify-space-between pt-sm-2">
                <div><v-card-title class="text-h5">Visión General Inversiones Activas</v-card-title></div>
                <div class="my-sm-0 my-2">
                    <v-select v-model="select" :items="items" variant="outlined" density="compact"
                        hide-details></v-select>
                </div>
            </div>
            <div class="mt-6">
                <apexchart type="bar" height="370px" :options="chartOptions.chartOptions" :series="chartOptions.series">
                </apexchart>
            </div>
        </v-card-item>
    </v-card>
</template>

