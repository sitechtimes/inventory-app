<template>
  <div id="popUpPanel" class="popUpPanel vendorPanel">
    <div class="chart1-cont">
      <div>
        <canvas id="myChart1"></canvas>
      </div>
      <div class="btn-cont">
        <button class="maximize-button" @click="maximizeChart()">
          <font-awesome-icon :icon="['fas', 'maximize']" />
        </button>
      </div>

    </div>

    <div class="no-show" ref="chart2">
      <div class="chart2-cont">
        <canvas id="myChart2"></canvas>
      </div>
      <button class="minimize-button" @click="maximizeChart()">
        <font-awesome-icon :icon="['fas', 'minimize']" />
      </button>
    </div>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart } from 'chart.js/auto';

const props = defineProps(["categoryName"])



const isMaximized = ref(false);
const chart2 = ref()
let CategoryItem = ref([])
let ItemCount = ref([])

const maximizeChart = () => {
  isMaximized.value = !isMaximized.value;
  if (isMaximized.value) {
    console.log(chart2.value)
    chart2.value.classList.remove('no-show')
    chart2.value.classList.add('fullScreen')
  } else if (!isMaximized.value) {
    chart2.value.classList.add('no-show')
    chart2.value.classList.remove('fullScreen')
  }
};
const chartData = ref({
  labels: CategoryItem.value,
  datasets: [
    {
      label: 'Total Stock Available',
      data: ItemCount.value,
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      backgroundColor: 'rgb(75, 1, 192)',
      tension: 0.1
    }
  ]
});

const chartOptions = ref({
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
    }, x: {
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
          if (typeof lbl === 'string' && lbl.length > 10) {
            labels[i] = lbl.substring(0, 10) + "..."; // cutting
          }
        }
      }
    },
  },
  plugins: {
    legend: {
      labels: {
        font: {
          size: 14
        }
      }
    }
  }
});


const createChart = () => {
  const ctx1 = document.getElementById('myChart1').getContext('2d');

  const chart1 = new Chart(ctx1, {
    type: 'bar',
    data: chartData.value,
    options: chartOptions.value,
  });

  const ctx2 = document.getElementById("myChart2").getContext('2d');

  const chart2 = new Chart(ctx2, {
    type: 'bar',
    data: chartData.value,
    options: chartOptions.value,
  });
};

onMounted(() => {
  fetchData();
});

async function fetchData() {
  try {
    const config = useRuntimeConfig()
    const response = await fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/category/`, {

      method: "GET",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
    });

    const data = await response.json();

    const CategoryName = props.categoryName
    data.forEach((category) => {
      console.log(category)
      if (CategoryName === category.category_name) {
        category.itemsCategory.forEach((item) => {
          CategoryItem.value.push(item.name)
          ItemCount.value.push(item.total)
        })
      }
    });

    createChart();
  } catch (error) {
    console.log("Error fetching data:", error);
  }
}

</script>

<style scoped>
.popUpPanel {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.no-show {
  display: none;
}

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
}

#myChart {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.chart2-cont {
  height: 800px;
  display: flex;
  justify-content: center;
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
  left: 50%;
  width: 8rem;
}

.maximize-button {
  width: 4rem;

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
