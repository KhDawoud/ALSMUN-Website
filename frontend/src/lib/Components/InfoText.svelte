<script lang="ts">
    export let image: string;
    export let title: string;
    export let paragraphA: string;
    export let paragraphB: string;
</script>



<div class="border rounded-lg shadow p-7 mx-4 md:mx-10">

  <div class="flex flex-col md:flex-row w-full">

    <div class="w-full md:w-1/2 mb-4 md:mb-0">
      <header class="ps-4">
        <h2 class="font-bold text-2xl mb-2"> {title} </h2>
        <hr class="border-b mb-5">
      </header>
      <p class="p-4">{paragraphA}</p>
    </div>

    <div class="w-full md:w-1/2">
      <div class="ms-4">
        <img src={image} alt="Topic" class="w-full h-auto">
      </div>
    </div>
  </div>

  <div class="w-full">
    <div class="p-4">
      <p>{paragraphB}</p>
    </div>
  </div>

</div>
