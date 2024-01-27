<script lang="ts">
  import NavBar from "../Components/NavBar.svelte";
  import Carousel from "../Components/Carousel.svelte";
  import Schedule1 from "../../assets/Schedule1.jpg"
  import Schedule2 from "../../assets/Schedule2.jpg"
  import Schedule3 from "../../assets/Schedule3.jpg"
  let images = [Schedule1, Schedule2, Schedule3]
</script>

<NavBar />
<div>
  <Carousel perPage = "1" duration = 600>
    {#each images as image}
      <div class = "flex items-center justify-center h-fit">
        <img src = {image}/>
      </div>
    {/each}
    <span slot="left-control" class= "text-9xl text-slate-700">&laquo;</span>
    <span slot="right-control" class ="text-9xl text-slate-700">&raquo;</span>
  </Carousel>
</div>