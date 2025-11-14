return {
    {
        "bjarneo/aether.nvim",
        name = "aether",
        priority = 1000,
        opts = {
            disable_italics = false,
            colors = {
                -- Monotone shades (base00-base07)
                base00 = "#1a2238", -- Default background
                base01 = "#48465a", -- Lighter background (status bars)
                base02 = "#222c44", -- Selection background
                base03 = "#5a5870", -- Comments, invisibles
                base04 = "#909090", -- Dark foreground
                base05 = "#cbcbcb", -- Default foreground
                base06 = "#cbcbcb", -- Light foreground
                base07 = "#909090", -- Light background

                -- Accent colors (base08-base0F)
                base08 = "#BD8767", -- Variables, errors, red
                base09 = "#dbb9a5", -- Integers, constants, orange
                base0A = "#b9a246", -- Classes, types, yellow
                base0B = "#184c55", -- Strings, green
                base0C = "#649FB6", -- Support, regex, cyan
                base0D = "#6874bb", -- Functions, keywords, blue
                base0E = "#434773", -- Keywords, storage, magenta
                base0F = "#baaf80", -- Deprecated, brown/yellow
            },
        },
        config = function(_, opts)
            require("aether").setup(opts)
            vim.cmd.colorscheme("aether")

            -- Enable hot reload
            require("aether.hotreload").setup()
        end,
    },
    {
        "LazyVim/LazyVim",
        opts = {
            colorscheme = "aether",
        },
    },
}
