<template>
  <div class="container">
    <div class="header itemHeader subheading">Vendors</div>
    <div class="content">
      <div class="buttons">
        <button
          v-for="data in vendor"
          :key="data"
          class="vendor-container"
          @click="showChartfuc(data.itemsVendor)"
        >
          <h1 class="vendor-name subheading">{{ data.vendor_name }}</h1>
        </button>
      </div>
      <div class="info canvas" v-show="showInfo" id="canvas" ref="canvas">
        <div class="extraInfoPanel">
          <div class="chart1-cont" ref="chart1">
            <div>
              <canvas id="cont1"></canvas>
            </div>
            <div class="btn-cont1">
              <button
                v-if="!minMax"
                @click="maximizeChart()"
                class="maximize-button"
              >
                <font-awesome-icon :icon="['fas', 'maximize']" />
              </button>
            </div>
          </div>
          <div class="no-show" ref="chart2">
            <div>
              <canvas id="cont2"></canvas>
              <button
                class="minimize-button"
                v-if="minMax"
                @click="maximizeChart()"
              >
                <font-awesome-icon :icon="['fas', 'minimize']" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { Chart } from "chart.js/auto";
import { useItemsStore } from "~/store/ItemsStore";

let showChart = ref(false);
let vendor = ref([]);
let chart1 = ref();
let chart2 = ref();
let showInfo = ref(false); // Step 1
let minMax = ref(false);
let canvas = ref();
let store = useItemsStore();

onMounted(() => {
  const config = useRuntimeConfig();
  fetch(
    `${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/vendor/`,
    {
      method: "GET",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
    }
  )
    .then((response) => response.json())
    .then((data) => {
      vendor.value = data;
    });
});

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: "Total Stock Available",
      data: [],
      fill: false,
      borderColor: "rgb(75, 192, 192)",
      backgroundColor: "rgb(75, 1, 192)",
      tension: 0.1,
    },
  ],
});

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
    },
    x: {
      ticks: {
        autoSkip: true,
        maxRotation: 80,
        minRotation: 80,
        fontSize: 16,
      },
      beforeUpdate(axis) {
        const labels = axis.chart.data.labels;
        for (let i = 0; i < labels.length; i++) {
          const lbl = labels[i];
          if (typeof lbl === "string" && lbl.length > 10) {
            labels[i] = lbl.substring(0, 10) + "..."; // cutting
          }
        }
      },
    },
  },
  plugins: {
    legend: {
      labels: {
        font: {
          size: 14,
        },
      },
    },
  },
});

function createChart() {
  const ctx1 = document.getElementById("cont1").getContext("2d");
  const chart1 = new Chart(ctx1, {
    type: "bar",
    data: chartData.value,
    options: chartOptions.value,
  });
  chart1 = chart1;

  const ctx2 = document.getElementById("cont2").getContext("2d");
  const chart2 = new Chart(ctx2, {
    type: "bar",
    data: chartData.value,
    options: chartOptions.value,
  });
  chart2 = chart2;
}

function updateChart(tag, quantity) {
  chart1.data.labels = tag;
  chart1.data.datasets[0].data = quantity;
  chart1.update();
  chart2.data.labels = tag;
  chart2.data.datasets[0].data = quantity;
  chart2.update();
}

const showChartfuc = (vendorItem) => {
  showInfo.value = true; // Step 3

  if (!showChart.value) {
    showChart.value = true;

    let labels = [];
    let quantity = [];
    vendorItem.forEach((item) => {
      labels.push(item.name);
      quantity.push(item.total);
    });
    createChart();
    updateChart(labels, quantity);
  } else if (showChart.value) {
    let labels = [];
    let quantity = [];
    vendorItem.forEach((item) => {
      labels.push(item.name);
      quantity.push(item.total);
    });
    updateChart(labels, quantity);
  }
  if (store.dismiss === false) {
    store.NavMenu();
  }
};

const maximizeChart = () => {
  isMaximized.value = !isMaximized.value;
  if (isMaximized.value) {
    console.log(chart2.value);
    chart2.value.classList.remove("no-show");
    chart2.value.classList.add("fullScreen");
  } else if (!isMaximized.value) {
    chart2.value.classList.add("no-show");
    chart2.value.classList.remove("fullScreen");
  }
};
</script>

<style scoped>
.fullScreen {
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 0;
  margin: 0;
  z-index: 9999;
  background-color: white;
  overflow: auto;
}
.no-show {
  display: none;
}
.container {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.header {
  text-align: center;
  font-size: 24px;
  padding: 20px;
}

.content {
  display: flex;
  flex-direction: row;
  padding-top: 3rem;
}

.buttons {
  flex: 1;
  margin-left: 5rem;
}

.info {
  flex: 1;
}

.bigdiv {
  display: flex;
  flex-flow: column nowrap;
}

.other-stuff {
  display: flex;
  flex-flow: row nowrap;
}

.chart-cont {
  height: 70rem;
  width: 70rem;
}

.vendors {
  display: flex;
  max-width: 60%;
  flex-flow: row wrap;
}

.vendor-container {
  border: var(--border);
  padding: 30px 55px 30px 55px;
  margin: 6px;
  width: 24rem;
  transition: all 0.2s;
  border-radius: 0.5rem;
}

.vendor-container:hover {
  background-color: var(--halflightgray);
  cursor: pointer;
}

.vendor-name {
  color: #333;
  font-size: 20px;
  margin: 0;
}

#Vendor {
  padding: 2vw;
  height: 100%;
  max-width: fit-content !important;
}
.canvas-cont {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  margin: 2rem;
  flex-grow: 1;
  min-height: 0;
}

.maximize-button,
.minimize-button {
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.minimize-button {
  position: relative;
  left: 45%;
  width: 8rem;
  margin-top: 100px;
}

.maximize-button {
  width: 8rem;
}

.maximize-button:hover,
.minimize-button:hover {
  background-color: #2980b9;
}

.maximize-button:active,
.minimize-button:active {
  background-color: #1f639e;
}

.btn-cont {
  display: flex;
  justify-content: flex-end;
  padding: 5px;
}

.chart-cont-big {
  height: 50rem;
  display: flex;
  justify-content: center;
}

@media only screen and (orientation: landscape) {
  .minimize-button {
    left: 45%;
    margin-bottom: 10vh;
  }
}

@media only screen and (orientation: landscape) and (max-height: 768px) {
  #Vendor {
    height: 55rem !important;
    width: fit-content !important;
  }
  .minimize-button {
    margin-top: 10vh;
  }
}

@media screen and (max-width: 912px) {
  #Vendor {
    height: 45rem !important;
    width: fit-content !important;
  }
}

@media screen and (max-width: 820px) {
  #Vendor {
    height: 60rem !important;
    width: fit-content !important;
  }
  .minimize-button {
    margin-top: 100px;
    left: 45%;
  }
}

@media screen and (max-width: 760px) {
  .content {
    flex-direction: column-reverse;
  }
  .chart-cont-small,
  .canvas-cont {
    max-width: 95%;
    margin-bottom: 3rem;
  }
  .canvas-cont,
  .buttons,
  .chart-cont-small {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
  }
  .chart-cont-big {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #Vendor {
    margin-top: 100px;
  }

  .minimize-button {
    position: relative;
    right: 0%;
    left: 0%;
  }
  .buttons {
    margin-left: 0;
  }
}

@media only screen and (max-width: 540px) {
  #Vendor {
    width: fit-content !important;
  }
}

@media screen and (max-width: 414px) {
  .canvas-cont {
    margin-top: 100px;
  }
  #Vendor {
    height: 20rem !important;
    width: fit-content !important;
  }
}

@media screen and (max-width: 280px) {
  #Vendor {
    height: 40rem !important;
    width: fit-content !important;
  }
}
</style>
