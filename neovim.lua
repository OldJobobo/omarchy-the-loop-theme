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
                base01 = "#182133", -- Lighter background (status bars)
                base02 = "#80889c", -- Selection background
                base03 = "#9586cf", -- Comments, invisibles
                base04 = "#afb6c5", -- Dark foreground
                base05 = "#afb6c5", -- Default foreground
                base06 = "#dde2eb", -- Light foreground
                base07 = "#dde2eb", -- Light background

                -- Accent colors (base08-base0F)
                base08 = "#cf9276", -- Variables, errors, red
                base09 = "#e2b099", -- Integers, constants, orange
                base0A = "#d4be68", -- Classes, types, yellow
                base0B = "#5f99a4", -- Strings, green
                base0C = "#77b7c8", -- Support, regex, cyan
                base0D = "#7f8fe0", -- Functions, keywords, blue
                base0E = "#9586cf", -- Keywords, storage, magenta
                base0F = "#e4d294", -- Deprecated, brown/yellow
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
