<script lang="ts">
    import { Link } from "svelte-routing";
    export let options: Object;
    export let text: string;
    export let dark: boolean;
    let clicked: boolean = false;
</script>

<div class="relative inline-block text-left">
  <div>
    <button on:click={() => clicked = !clicked} type="button" class="{dark ? "bg-gray-800 text-gray-300 hover:bg-gray-700":"bg-white text-gray-900 hover:bg-gray-50"} inline-flex w-full justify-center gap-x-1.5 rounded-md px-3 py-2 font-medium ring-gray-300 hover:bg-gray-50" id="menu-button" aria-expanded="true" aria-haspopup="true">
      {text}
      <svg class="-mr-1 h-5 w-5 text-gray-400 mt-1" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
        <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
      </svg>
    </button>
  </div>

  {#if clicked}
    <div class="absolute left-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
        <div class="py-1" role="none">
            <!-- Active: "bg-gray-100 text-gray-900", Not Active: "text-gray-700" -->
            {#each Object.entries(options) as [name, link], i (i)}
                <Link to={link} class="text-gray-700 block px-4 py-2 text-sm hover:text-gray-900 hover:bg-gray-100" role="menuitem">{name} </Link>
            {/each}    
        </div>
    </div>
  {/if}
</div>