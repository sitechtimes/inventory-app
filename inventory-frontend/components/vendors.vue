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
          <div class="chart1-cont">
            <div ref="chart1">
              <canvas class="canvas1" id="cont1"></canvas>
            </div>
            <div class="btn-cont1">
              <button @click="maximizeChart()" class="maximize-button">
                <font-awesome-icon :icon="['fas', 'maximize']" />
              </button>
            </div>
          </div>
          <div class="no-show" ref="chart2">
            <div>
              <canvas class="canvas2" id="cont2"></canvas>
              <button class="minimize-button" @click="maximizeChart()">
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
import { getRelativePosition } from "chart.js/helpers";

let showChart = ref(false);
let vendor = ref([]);
let chart1 = ref(null);
let chart2 = ref(null);
let showInfo = ref(false); // Step 1
let canvas = ref();
let store = useItemsStore();
let isMaximized = ref(false);

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
      backgroundColor: "rgb(32, 116, 180)",
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
  /*   onClick: (e) => {
    let smallChart = chart1.value;
    console.log(smallChart);
    console.log(Chart.helpers.getRelativePosition(e));
    const canvasPosition = Chart.helpers.getRelativePosition(e, smallChart); // cant seem to get the chart still.
    const dataX = smallChart.value.scales.x.getValueForPixel(canvasPosition.x); //gets the x value of the mouseclick
    console.log(dataX);
  }, */
});

function createChart() {
  const ctx1 = document.getElementById("cont1").getContext("2d");
  let tempchart1 = new Chart(ctx1, {
    type: "bar",
    data: chartData.value,
    options: {
      ...chartOptions.value,
      onClick: (e) => {
        let smallChart = Chart.getChart("cont1");
        const canvasPosition = getRelativePosition(e, smallChart); // cant seem to get the chart still.
        const dataX = smallChart.scales.x.getValueForPixel(canvasPosition.x); //gets the x value of the mouseclick
        console.log(dataX);
      },
    },
  });

  const ctx2 = document.getElementById("cont2").getContext("2d");
  let tempchart2 = new Chart(ctx2, {
    type: "bar",
    data: chartData.value,
    options: chartOptions.value,
  });

  chart1.value = tempchart1;
  chart2.value = tempchart2;
}

function updateChart(tag, quantity) {
  Chart.getChart("cont1").data.labels = tag;
  Chart.getChart("cont1").data.datasets[0].data = quantity;
  Chart.getChart("cont2").data.labels = tag;
  Chart.getChart("cont2").data.datasets[0].data = quantity;
  Chart.getChart("cont1").update();
  Chart.getChart("cont2").update();
}

const showChartfuc = (vendorItem) => {
  console.log(vendorItem);
  showInfo.value = true; // Step 3
  showChart.value = true;
  if (!Chart.getChart("cont1")) {
    createChart();
  }
  let labels = [];
  let quantity = [];
  vendorItem.forEach((item) => {
    labels.push(item.name);
    quantity.push(item.total);
  });
  updateChart(labels, quantity);
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
  height: 100vh !important;
}

.canvas2 {
  height: 90vh !important;
  width: fit-content;
  position: relative;
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
.other-stuff {
  display: flex;
  flex-flow: row nowrap;
}
.vendor-name {
  color: #333;
  font-size: 20px;
  margin: 0;
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
</style>
