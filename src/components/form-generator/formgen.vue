<template>
  <v-container fluid>
    <v-card>
      <v-card-title class="py-4 pb-6 text-h5 text-center">{{ config.title }}</v-card-title>
      <v-card-text>
        <v-row v-if="config.cond1">
          <template v-for="(cond1, index1) in config.cond1" :key="`cond1-${index1}`">
            <v-col cols="1" class="d-flex flex-column justify-center ">
              <h4 class="text-center custom-h4"
                  :class="index1 === 0 ? 'green--text' : 'orange--text'"
                  style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{{ cond1 }}</h4>
            </v-col>
            <v-col cols="5" class="pa-3 rounded-lg" :class="index1 === 0 ? 'background-green' : 'background-orange'">
              <v-row v-if="config.cond2" v-for="(cond2, index2) in config.cond2" :key="`cond2-${index2}`">
                <v-col cols="12">
                  <h5 class="red--text text-center"
                       style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{{ cond2 }}</h5>
                  <v-row v-if="config.cond3">
                    <template v-for="(cond3, index3) in config.cond3" :key="`cond3-${index3}`">
                      <v-col cols="6">
                        <v-text-field v-if="config.type === 'text' || !config.type" dense :label="cond3" outlined v-model="values[cond1][cond2][cond3]"></v-text-field>
                        <v-textarea v-else-if="config.type === 'textarea'" :label="cond3" outlined v-model="values[cond1][cond2][cond3]"></v-textarea>
                        <v-date-picker v-else-if="config.type === 'date'" v-model="values[cond1][cond2][cond3]"></v-date-picker>
                        <v-text-field v-else-if="config.type === 'number'" type="number" :label="cond3" outlined v-model="values[cond1][cond2][cond3]"></v-text-field>
                        <v-checkbox v-else-if="config.type === 'checkbox'" :label="cond3" v-model="values[cond1][cond2][cond3]"></v-checkbox>
                      </v-col>
                    </template>
                  </v-row>
                  <v-text-field v-else outlined v-model="values[cond1][cond2]"></v-text-field>
                </v-col>
              </v-row>
              <v-text-field v-else outlined v-model="values[cond1]"></v-text-field>
            </v-col>
          </template>
        </v-row>
        
        <v-row v-else align="center">

          <v-col>
            <v-select v-if="config.type === 'dropdown'" :items="config.items" label="Selecciona" outlined v-model="values[config.title]"></v-select>
            <v-text-field v-else-if="config.type === 'text' || !config.type" label="" outlined v-model="values[config.title]"></v-text-field>
            <v-textarea v-else-if="config.type === 'textarea'" label="" outlined v-model="values[config.title]"></v-textarea>
            <v-text-field v-else-if="config.type === 'date'" type="date" label="Fecha" outlined v-model="values[config.title]"></v-text-field>
            <v-text-field v-else-if="config.type === 'number'" type="number" @keypress="onlyNumber($event)" label="Ingresa número aquí" outlined v-model="values[config.title]"></v-text-field>
            <v-checkbox v-else-if="config.type === 'checkbox'" v-for="(item, index) in config.items" :key="index" :label="item" v-model="values[config.title][item]"></v-checkbox>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>


<script>
export default{
  props: {
    config: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      values: {}
    };
  },
  created() {
    if (this.config.cond1) {
      let conditions = [this.config.cond1, this.config.cond2, this.config.cond3].filter(Boolean);
      let values = this.config.value || [];
      let valueCounter = { index: 0 };
      let createDataModel = (conditions, model, valueCounter) => {
        let condition = conditions[0];
        let nextConditions = conditions.slice(1);
        for (let j = 0; j < condition.length; j++) {
          let key = condition[j];
          if (nextConditions.length === 0) {
            model[key] = values[valueCounter.index] || '';
            valueCounter.index++;
          } else {
            model[key] = {};
            createDataModel(nextConditions, model[key], valueCounter);
          }
        }
      };
      createDataModel(conditions, this.values, valueCounter);
    } else {
      if (this.config.type === 'checkbox') {
        this.values[this.config.title] = this.config.items.reduce((acc, curr) => {
          acc[curr] = this.config.value.includes(curr);
          return acc;
        }, {});
      } else {
        this.values[this.config.title] = this.config.value || '';
      }
    }
  },
  methods: {
    onlyNumber($event) {
      let keyCode = ($event.keyCode ? $event.keyCode : $event.which);
      if ((keyCode < 48 || keyCode > 57) && keyCode !== 46) { // 46 is the ASCII of '.'
        $event.preventDefault();
      }
    },
    getFormData() {
      return this.values;
    }
  }
};
</script>

  <style>
  .background-green {
    background-color: #e8f5e9;
  }
  .background-orange {
    background-color: #fff8e1;
  }
  .v-input__details {
    display: none;
  }

  </style>
  