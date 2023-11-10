<script lang="ts">
  import { Link } from "svelte-routing";

  export let text: string | null;
  export let image: string;
  export let header: string;
  export let link: string;
  export let noReadMe: boolean | undefined;

  text = !text ? "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." : text

</script>




<section class="grid grid-cols-1 md:grid-cols-2 gap-4 ">
    <div class="relative flex items-end">
        <img src={image} alt={header} class="object-cover  w-full"/>
    </div>
    <div class="pt-3 pb-5 md:py-6 px-9 flex flex-col justify-between">
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
            {#if !noReadMe}
                <Link to={link} class="bg-blue-600 hover:bg-blue-800 rounded-md text-white px-3 py-1 shadow-md">
                    Read More
                </Link>
            {/if}
        </div>
    </div>
</section>
<hr>