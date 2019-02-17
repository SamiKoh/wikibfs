<template>
  <div class="container">
    <h1 class="primary">Shortest path between two Wikipedia pages</h1>
    <h3 class="time">Time taken: {{minutes}} minutes {{seconds}} seconds.</h3>
    <form>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <label class="input-group-text" for="inputGroupSelect01">Wikipedia language</label>
        </div>
        <select class="custom-select" id="inputGroupSelect01" v-model="language">
          <option value="en">English</option>
          <option value="fi">Finnish</option>
          <option value="de">German</option>
        </select>
      </div>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <label class="input-group-text" for="from">From page</label>
        </div>
        <div class="input-group-prepend light">
          <span class="input-group-text light">https://{{language}}.wikipedia.org/wiki/</span>
        </div>
        <input id="from" type="text" class="form-control">
      </div>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <label class="input-group-text" for="to">To page</label>
        </div>
        <div class="input-group-prepend light">
          <span class="input-group-text light">https://{{language}}.wikipedia.org/wiki/</span>
        </div>
        <input id="to" type="text" class="form-control">
      </div>
      <button class="btn btn-primary" @click="search">Go!</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      time: 0,
      minutes: 0,
      seconds: 0,
      language: 'en',
      startTime: Date,
    };
  },
  methods: {
    search(e) {
      this.startTime = new Date();
      const tmr = this.timer;
      console.log('language ', this.language);
      setTimeout(tmr, 1000);
      e.preventDefault();
    },
    timer() {
      const t = new Date() - this.startTime;
      const sec = t / 1000;
      this.minutes = Math.floor(sec / 60);
      this.seconds = Math.round(sec % 60);
      console.log(t);
    },
  },
};
</script>


<style lang="scss" scoped>
button {
  margin-top: 2em;
}
h3 {
  margin-top: 1em;
}
form {
  margin-top: 2em;
}
.input-group > .input-group-prepend {
  flex: 0 0 15%;
}
.input-group .input-group-text {
  width: 100%;
}
.light {
  background-color: #fff !important;
  border-right-color: #fff !important;
}
</style>
