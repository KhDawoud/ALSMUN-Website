<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import Banner from "../../Components/Banner.svelte";
    import JazminBlaj from "../../../assets/Secretariat/Jazmin Blaj.jpg"
    import MariamElRamly from "../../../assets/Secretariat/Mariam Elramly.jpg"
    import IbrahimZineldin from "../../../assets/Secretariat/Ibrahim Zineldin - DSG.jpg"
    import AdhamFayed from "../../../assets/Secretariat/Adham Fayed - USG.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
    import JBSignature from "../../../assets/Signatures/JB.png";
  </script>
  
  
  <NavBar />
  <header class="px-10">
      <h1 class=" text-4xl font-bold text-center mt-10"> Our Secretariat </h1>
      <hr class="mb-2 mt-4">  
  </header>
  <main class=" grid-flow-row grid-rows-4 m-5 space-y-4 p-5">
        <GroupSection link={null} noReadMe={true} header="Jazmin Blaj - Secretary General" text="Hey delegates! I’m Jazmin.

            It is a pleasure to act as your Secretary General this ALSMUN and will be an even greater pleasure to watch you all thrive and succeed at this conference. 
            I started off as a shy delegate 5 years ago, unsure of how my thoughts and opinions could or should be presented to others. MUN has helped me greatly to mould this skill and now I proudly hold my experiences at heart for the person I have grown to be. 
            
            I cannot wait to see you all!
            " image={JazminBlaj} signature={JBSignature}/>
        <GroupSection link={null} noReadMe={true} header="Ibrahim Zineldin - Deputy Secretary General" text={null} image={IbrahimZineldin} />
        <GroupSection link={null} noReadMe={true} header="Adham Fayed - Under Secretary General" text={null} image={AdhamFayed} />
        <GroupSection link={null} noReadMe={true} header="Mariam ElRamly - Assistant Secretary General" text="Hi! My name’s Mariam and I’m this year’s ALSMUNII Assistant Secretary General. " image={MariamElRamly} />
  </main>