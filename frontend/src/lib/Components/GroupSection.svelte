<script lang="ts">
  import { Link } from "svelte-routing";

  export let text: string | null;
  export let image: string;
  export let header: string;
  export let link: string | null;
  export let noReadMe: boolean | undefined;
  export let signature: undefined | string; 

  text = !text ? "Welcome to ALSMUNII! We can't wait to see you!" : text

</script>




<section class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="relative flex">
        <img src={image} alt={header} class="object-cover w-full"/>
    </div>
    <div class="pt-3 pb-5 md:py-6 md:px-7 px-4 flex flex-col justify-between">
        <div class="mb-4 md:mb-0">
            <div class="font-bold text-2xl text-gray-800 mb-3">
                <header>{header}</header>
                <hr>
            </div>
            <div>
                <article class=" text-sm md:text-base">
                    {text}
                </article>
            </div>
        </div> 

        <div>
            {#if !noReadMe && link != null}
                <Link to={link} class="bg-blue-600 hover:bg-blue-800 rounded-md text-white px-3 py-1 shadow-md">
                    Read More
                </Link>
            {:else if signature}
                <div>
                    <img src={signature} alt="Signature" width=70>
                </div>
            {/if}
        </div>
    </div>
</section>
<hr>