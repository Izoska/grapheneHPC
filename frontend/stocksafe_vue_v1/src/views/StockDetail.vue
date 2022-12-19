
<template>
  <div>
    <!-- Begin Page Content -->
    <div class="container-fluid">
      <!-- Page Heading -->
      <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">
          {{ stockdetailinfo.stockName }}
          <b-icon
            v-if="!myStock_tag"
            class="mb-2 mx-1 staricon2"
            icon="bag"
            variant="secondary"
            @click="addMyStock()"
          ></b-icon>
          <b-icon
            v-else
            class="mb-2 mx-1 staricon2"
            icon="bag-fill"
            variant="info"
            @click="deleteMyStock()"
          ></b-icon>
          <b-icon