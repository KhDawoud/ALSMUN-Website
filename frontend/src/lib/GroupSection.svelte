<script lang="ts">
  import { Link } from "svelte-routing";

  export let text: string;
  export let image: string;
  export let header: string;
  export let link: string;

</script>




<section class="grid grid-cols-1 md:grid-cols-2 gap-4 border-2 border-gray-400 rounded-3xl shadow-md">
    <div class="relative flex items-end">
        <img src={image} alt={header} class="object-cover rounded-[1.35rem] rounded-b-none md:rounded-e-none md:rounded-[1.35rem] w-full"/>
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
            <Link to={link} class="bg-blue-600 hover:bg-blue-800 rounded-md text-white px-3 py-1 shadow-md">
                Read More
            </Link>
        </div>
    </div>
</section>